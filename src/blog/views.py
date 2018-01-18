from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Moduły stronicowania
from django.views.generic import ListView # Widok klasy
from .forms import EmailPostForm, CommentForm #Funkcja email i komenatrzy
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# Funkcja email
def post_share(request, post_id):
    # Pobieranie posta z jego ID
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Formularz został wysłany.
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) zachęca do przeczytania "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Przeczytaj post "{}" na stronie {}\n\n Komentarz dodany przez {}: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'django.nauka@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})

def post_list(request, tag_slug=None): # Widok listy ze stronicowaniem i tagami
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag =           get_object_or_404(Tag, slug=tag_slug)
        object_list =   object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) # 3 Posty na każdą stronę
    page =      request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # W razie błędu pobierania listy wyników pokaż pierwszą stronę
        posts = paginator.page(1)
    except EmptyPage:
        # W razie braku danej strony, wczytaj ostatnią
        posts = paginator.page(paginator.num_pages)
    
    context = {
              'page': page, 
              'posts': posts, 
              'tag': tag
              }
    return render(request, 'blog/post/list.html', context)

# Widok szczegółów
def post_detail(request, year, month, day, post):
    
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True) # Lista komenatrzy

    # Niezdefiniowane obiekty przez pominięty 'if request.method' wciąż muszą być przesłane przez 'return render...'
    # co generuje błąd: "UnboundLocalError: local variable referenced before assignment"
    # Biorąc pod uwagę iż przesyłane obiekty do templatki są if'owane, należy je zdefiniować pod wynik FALSE, aby 'return render...'
    # mógł je przesłać, ale żeby nie wprowadzały logiki templatki w błąd. W dalszym etapie obiekty te po wykonaniu ifa są nadpisywane
    # poprawnymi wartościami.
    comment_form = ''
    new_comment = ''

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()

    # Lista podobnych postów
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    context =  {
                'post': post, 
                'comments': comments, 
                'comment_form': comment_form, 
                'new_comment': new_comment, 
                'similar_posts': similar_posts
                }
    return render(request, 'blog/post/detail.html', context)




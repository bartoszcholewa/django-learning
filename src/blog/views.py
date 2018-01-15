from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Moduły stronicowania
from django.views.generic import ListView # Widok klasy

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
def post_list(request): # Widok listy ze stronicowaniem
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 Posty na każdą stronę
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # W razie błędu pobierania listy wyników pokaż pierwszą stronę
        posts = paginator.page(1)
    except EmptyPage:
        # W razie braku danej strony, wczytaj ostatnią
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})

# Widok szczegółów
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish_year=year, publish_month=month, publish_day=day)
    return render(request, 'blog/post/detail.html', {'post': post})




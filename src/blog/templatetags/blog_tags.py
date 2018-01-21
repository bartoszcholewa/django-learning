from django import template
register = template.Library() # wciągnij biblioteki do tworzenia własnych filtów i znaczników pod [register]
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

# Rodzaje własnych znaczników szablonu:
# simple_tag() - Przetworzenie danych i zwrot ciągu tekstowego,
# inclusion_tag() - Przetworzenie danych i zwrot wygenerowanego szablonu,
# assignment_tag() - Przetworzenie danych i ustawienie zmiennej w kontekście.

# Ilość opublikowanych postów
@register.simple_tag                # zarejestruj prosty znacznik [template.Library().simple_tag]
def total_posts():                  # o nazwie total_posts
    return Post.published.count()   # który zwraca ilość [count] opublikowanych [published] postów[Post]

# Najnowsze posty
@register.inclusion_tag('blog/post/latest_posts.html')              # zarejestruj znacznik [template.Library().inclusion_tag] i wygeneruj szablon [latest_posts.html]
def show_latest_posts(count=5):                                     # o nazwie show_latest_post który akceptuje opcjonalny paraments [count] z domyślną wartością [5]
    latest_posts = Post.published.order_by('-publish')[:count]      # poczym wciągnij 5 postów [:count] które są opublikowane [published] po dacie od najnowszego ['-publish'] 
    return {'latest_posts': latest_posts}                           # i zwróć je jako słownik zmiennych który zostanie użyty jako kontekst do wygenerowania szablonu [latest_posts.html]

# Najbardziej komentowane posty
@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

# Własny filtr szablonu Markdown
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
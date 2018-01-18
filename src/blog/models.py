from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager): #Utworzenie menedżerów modelu
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')
    
class Post(models.Model): # Dodawanie postów na bloga
    STATUS_CHOICES =    (('draft', 'Roboczy'), ('published', 'Opublikowany'),)
    title =             models.CharField(max_length=250)
    slug =              models.SlugField(max_length=250, unique_for_date='publish')
    author =            models.ForeignKey(User, related_name='blog_posts')
    body =              models.TextField()
    publish =           models.DateTimeField(default=timezone.now)
    created =           models.DateTimeField(auto_now_add=True)
    updated =           models.DateTimeField(auto_now=True)
    status =            models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects =           models.Manager() # Menedżer domyślny
    published =         PublishedManager()  # Menedżer niestandardowy
    tags =              TaggableManager()
    
    class Meta: #Sortowanie opublikowanych
        ordering = ('-publish',)
        
    def __str__(self): #Wyświetlanie nazwy posta w Admin
        return self.title

    def get_absolute_url(self): #Uzyskiwanie pełnego adresu strony
        return reverse('blog:post_detail', 
                        args=[
                            self.publish.year, 
                            self.publish.strftime('%m'), 
                            self.publish.strftime('%d'), 
                            self.slug
                            ])

class Comment(models.Model): # System komentarzy
    post =      models.ForeignKey(Post, related_name='comments')
    name =      models.CharField(max_length=80)
    email =     models.EmailField()
    body =      models.TextField()
    created =   models.DateTimeField(auto_now_add=True)
    updated =   models.DateTimeField(auto_now=True)
    active =    models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Komentarz dodany przez {} dla posta {}'.format(self.name, self.post)

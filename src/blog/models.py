from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

#Utworzenie menedżerów modelu
class PublishedManager(models.Manager): 
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# Dodawanie postów na bloga
class Post(models.Model): 
    STATUS_CHOICES =    (('draft', 'Roboczy'), ('published', 'Opublikowany'),)
    title =             models.CharField(max_length=250)
    slug =              models.SlugField(max_length=250, unique_for_date='publish')
    author =            models.ForeignKey(User, related_name='blog_posts')
    body =              models.TextField()
    publish =           models.DateTimeField(default=timezone.now)
    created =           models.DateTimeField(auto_now_add=True)
    updated =           models.DateTimeField(auto_now=True)
    status =            models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects =           models.Manager()    # Menedżer domyślny
    published =         PublishedManager()  # Menedżer niestandardowy
    tags =              TaggableManager()

    #Sortowanie opublikowanych
    class Meta:
        ordering = ('-publish',)

    #Wyświetlanie nazwy posta w Admin    
    def __str__(self):
        return self.title
    
     #Uzyskiwanie pełnego adresu strony
    def get_absolute_url(self):
        return reverse('blog:post_detail', 
                        args=[
                            self.publish.year, 
                            self.publish.strftime('%m'), 
                            self.publish.strftime('%d'), 
                            self.slug
                            ])

# System komentarzy
class Comment(models.Model): 
    post =      models.ForeignKey(Post, related_name='comments')
    name =      models.CharField(max_length=80)
    email =     models.EmailField()
    body =      models.TextField()
    created =   models.DateTimeField(auto_now_add=True)
    updated =   models.DateTimeField(auto_now=True)
    active =    models.BooleanField(default=True)

    # Sortowanie stworzonych
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Komentarz dodany przez {} dla posta {}'.format(self.name, self.post)

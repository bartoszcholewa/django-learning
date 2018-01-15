from django.conf.urls import url
from . import views

# Dodanie wzorców adresów URL do widoków

urlpatterns = [
    # Widok posta
    url(r'^$', views.PostListView.as_view(), name='post_list'), #url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
        r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
]
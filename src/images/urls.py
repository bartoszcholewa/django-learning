from django.conf.urls import url
from .views import image_create, image_detail, image_like

urlpatterns = [
    url(r'^create/$', image_create, name='create'),
    url(r'detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', image_detail, name='detail'),
    url(r'^like/$', image_like, name='like'),
]
from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'track/$', trackView, name='track')
]
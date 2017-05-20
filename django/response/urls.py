from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'view/$', responseTable, name='response'),
    url(r'track/$', trackView, name='track')
]
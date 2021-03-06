from django.conf.urls import url
from django.views.generic import TemplateView
from views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='response/index.html'), name='index'),
    url(r'view/$', responseTable, name='view'),
    url(r'track/$', trackView, name='track')
]
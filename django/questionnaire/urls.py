from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<qid>[0-9]+)/$', views.questionView, name='question'),

]
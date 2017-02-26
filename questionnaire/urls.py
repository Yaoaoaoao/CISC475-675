from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<subject_code>[0-9]+)/$', views.patient, name='patient')
]

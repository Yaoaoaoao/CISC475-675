from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<qid>[0-9]+)/patient_id/(?P<patient_id>[0-9]+)/$', views.questionView, name='view'),
    url(r'^patient_id/(?P<patient_id>[0-9]+)/submit/$', views.submitAnswers, name='submit'),
]
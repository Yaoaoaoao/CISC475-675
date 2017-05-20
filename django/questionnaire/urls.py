from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^entry/patient_id/(?P<patient_id>[\d\w]+)$', entryView, name='entry'),
    url(r'^(?P<qid>[0-9]+)/patient_id/(?P<patient_id>[\d\w]+)/$', questionView, name='view'),
    url(r'^(?P<qid>[0-9]+)/patient_id/(?P<patient_id>[\d\w]+)/submit/$', submitAnswers, name='submit'),
    url(r'^about/$', TemplateView.as_view(template_name='questionnaire/about.html'), name='about'),

    url(r'login/$', auth_views.login, {'template_name': 'questionnaire/login.html'}, name='login'),
    url(r'logout/$', auth_views.logout, {'template_name': 'questionnaire/logout.html'}, name='logout'),
]
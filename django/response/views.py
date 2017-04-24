from django.http import HttpResponse
from django import forms
from questionnaire.models import Answer, Questionnaire
from django.shortcuts import render

QUESTIONNAIRES = Questionnaire.objects.all().values_list('id', 'title')
QUESTIONNAIRE_CHOICES = [('All', 'All')] + list(QUESTIONNAIRES)


class ResponseForm(forms.Form):
    questionnaire = forms.IntegerField(
        widget=forms.Select(choices=QUESTIONNAIRE_CHOICES),
    )
    patient_id = forms.IntegerField()
    date_from = forms.DateField()
    date_to = forms.DateField()


def index(request):
    form = ResponseForm()
    return render(request, 'response/index.html', {'form': form})

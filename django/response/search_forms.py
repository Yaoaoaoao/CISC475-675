from django import forms
from questionnaire.models import Answer, Questionnaire

QUESTIONNAIRES = Questionnaire.objects.all().values_list('id', 'title')
QUESTIONNAIRE_CHOICES = [('All', 'All')] + list(QUESTIONNAIRES)


class ResponseForm(forms.Form):
    questionnaire = forms.ChoiceField(
        choices=QUESTIONNAIRE_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    patient_id = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    date_from = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

from django.http import HttpResponse
from django.template import loader
from django.db.models import F
from .models import *

# Create your views here.

def index(request):
    ps = Patient.objects.all()
    print(ps)
    template = loader.get_template('questionnaire/index.html')
    context = { 'ps' : ps}
    return HttpResponse(template.render(context, request))

def patient(request, subject_code):
    patient = Patient.objects.get(subject_code = subject_code)
    print(patient)
    questionnaire = Questionnaire.objects.filter(patient = patient)
    print(len(questionnaire))
    d = {}
    for q in questionnaire:
        v = Answer.objects.filter(questionnaire = q)
        print(q,v)
        d[q] = v
    template = loader.get_template('questionnaire/patient.html')
    print(d)
    context = { 'patient' : patient, 'data': d}
    return HttpResponse(template.render(context, request))

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.utils import timezone
from threading import local
import pytz
from django.conf import settings
from django.db import IntegrityError
from datetime import datetime, timedelta, tzinfo

def index(request):
    return HttpResponse("You're looking at question.")


def questionView(request, qid, patient_id):
    context = {'questionnaire': None,
               'patient_id': None,
               'questions': []}

    context['questionnaire'] = Questionnaire.objects.get(id=qid)
    context['patient_id'] = int(patient_id)

    questions = Question.objects.filter(questionnaire__id=qid).order_by(
        'question_order')
    for question in questions:
        qobj = {'id': question.id,
                'order': question.question_order,
                'question_text': question.question_text,
                'type': question.question_type,
                'options': Option.objects.filter(
                    Q(question__id=question.id) & Q(option_order__gt=0))
                    .order_by('option_order'),
                }

        if qobj['type'] == 'SCALE':
            # Option order == -1 is the left label.
            # Option order == 0 is the right label. 
            qobj['labels'] = Option.objects.filter(
                Q(question__id=question.id) & Q(option_order__lte=0)
            ).values_list('option_text', flat=True).order_by('option_order')

        context['questions'].append(qobj)
    return render(request, 'questionnaire/question.html', context)


def submitAnswers(request, patient_id):
    """ 
        If submit is successful, return 
            {"status": true, "patient_id": xxx, "submit_date": today's date}
        If submit fails, return 
            {"status": true, "patient_id": xxx, "submit_date": today's date, 
             "error_msg": msg}
    """
    template = 'questionnaire/submit.html'
    submit_date = timezone.now()
    print submit_date
    context = {
        'patient_id': patient_id,
        'submit_date': submit_date,
        'status': False
    }

    if request.method == "POST":
        print request.POST
        try:
            for question_id, response in request.POST.iteritems():
                if question_id == "csrfmiddlewaretoken":
                    continue
                answer = Answer(question=Question.objects.get(pk=question_id),
                                submit_date=submit_date,
                                patient_id=patient_id,
                                response=response,
                                note="")
                answer.save()
            context['status'] = True
        except IntegrityError as e:
            context['error_msg'] = e.message

    else:
        context['error_msg'] = 'Form is invalid.'

    return render(request, template, context)

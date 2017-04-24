from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.db.models import Q
import datetime

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
        qobj = {'order': question.question_order,
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

def submitAnswers(request, qid, patient_id):
    if request.method == "POST" :
        for question_id in request.POST:
            if question_id == "csrfmiddlewaretoken":
                continue
            answer = Answer(question=Question.objects.get(pk=question_id), 
                            submit_date=datetime.datetime.now(),
                            patient_id=patient_id, 
                            response=request.POST[question_id],
                            note="")
            answer.save()

    print Answer.objects.filter(patient_id = patient_id)
    return HttpResponse("Upload successfully")
#    return HttpResponseRedirect(reverse('questionnaire:results', args=(qid, patient_id,)))

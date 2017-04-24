from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from questionnaire.models import *
from django.db.models import Q
import datetime
from datetime import datetime
from django.urls import reverse
from django.db.models import Count


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def querySubmit(request, qid, patient_id, year1, year2, month1, month2, day1, day2):
#    Answer.objects.filter(Q(patient_id=patient_id) & Q(date__range=["2011-01-01", "2011-01-31"]))
    date_from = datetime(int(year1), int(month1), int(day1))
    date_to = datetime(int(year2), int(month2), int(day2))
    '''
    answers = Answer.objects.annotate(Count('response'))
    print(answers)
    '''
    answers = Answer.objects.filter(Q(patient_id=patient_id) & Q(submit_date__gte=date_from) & Q(submit_date__lte=date_to))
#    print(answers)
    print(answers.annotate(Count('submit_date')))

    context = {'patient_id': None,
               'answers': [],}
    '''
    for answer in Answer.objects.all():

        qobj = {'questionnaire': answer.question.questionnaire.id,
                'patient_id': answer.patient_id,
                'submit_date': answer.submit_date,
                'question_order': answer.question.question_order,
                'question_id': answer.question.id,
                #                'score': Option.objects.filter(Q(question__id=answer.question.id) & Q(option_order=answer.response)),
                }
        print(answer.question.questionnaire.id)
        print(answer.submit_date)
    '''

    return HttpResponse('I am in query')

'''
def viewAll(request):

    for answer in Answer.objects.raw('SELECT * FROM Answer GROUP BY submit_date'):
        print(answer.submit_date)
    q = Answer.objects.all().annotate(patientid=Count('patient_id'))
    print(Answer.objects.values('submit_date').annotate(Count('submit_date')))
    print(Answer.objects.values('patient_id').annotate(Count('patient_id')))

#    print(Answer.objects.annotate(Answer('submit_date')))
#    for answer in Answer.objects.all().annotate(submit_date=Answer('submit_date')):
#        for each_log in answer:
#            print(each_log)
#        print(answer)
#        print(answer.submit_date)

    context = {'questionnaire_1': [],
               'questionnaire_2': []}

    for answer in Answer.objects.all():

        qobj = {'questionnaire': answer.question.questionnaire.id,
                'patient_id': answer.patient_id,
                'submit_date': answer.submit_date,
                'question_order': answer.question.question_order,
                'question_id': answer.question.id,
#                'score': Option.objects.filter(Q(question__id=answer.question.id) & Q(option_order=answer.response)),
                }
        if qobj['questionnaire'] == 1:
            context['questionnaire_1'].append(qobj)
        else:
            context['questionnaire_2'].append(qobj)
        print(answer.question.questionnaire.id)
        print(answer.submit_date)

    return HttpResponse(context)
'''
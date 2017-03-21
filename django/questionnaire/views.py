from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q


def index(request):
    return HttpResponse("You're looking at question.")


def questionView(request, qid):
    context = {'questionnaire': None,
               'questions': []}

    context['questionnaire'] = Questionnaire.objects.get(id=qid)

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

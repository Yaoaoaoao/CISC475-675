from django.http import HttpResponse
from django.shortcuts import render
from models import *


def index(request):
    return HttpResponse("You're looking at question.")


def questionView(request, qid):
    questions = Question.objects.filter(questionnaire__id=qid).order_by('question_order')
    context = {'questionnaire': []}
    for question in questions:
        qobj = {'order': question.id,
                'question_text': question.question_text,
                'type': question.question_type,
                'options': Option.objects.filter(question__id=question.id).order_by('option_order')
                }

        context['questionnaire'].append(qobj)

    return render(request, 'questionnaire/question.html', context)

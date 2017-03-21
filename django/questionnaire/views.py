from django.http import HttpResponse
from django.shortcuts import render
from models import *


def index(request):
    return HttpResponse("You're looking at question.")


def questionView(request, qid):
    questionnaire = Questionnaire.objects.get(id=qid)
    questions = Question.objects.filter(questionnaire__id=qid).order_by(
        'question_order')
    context = {'questionnaire': questionnaire,
               'questions': []}
    for question in questions:
        qobj = {'order': question.id,
                'question_text': question.question_text,
                'type': question.question_type,
                'options': Option.objects.filter(
                    question__id=question.id).order_by('option_order')
                }

        context['questions'].append(qobj)

    return render(request, 'questionnaire/question.html', context)

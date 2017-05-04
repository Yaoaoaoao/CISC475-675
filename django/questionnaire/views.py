from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from questionnaire.models import *
from django.db.models import Q
from django.utils import timezone
from django.db import IntegrityError


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


def submitAnswers(request, qid, patient_id):
    """ 
        If submit is successful, return 
            {"status": true, "patient_id": xxx, "submit_date": today's date}
        If submit fails, return 
            {"status": true, "patient_id": xxx, "submit_date": today's date, 
             "error_msg": msg}
    """
    template = 'questionnaire/submit.html'
    submit_date = timezone.now()
    context = {
        'patient_id': patient_id,
        'submit_date': submit_date,
        'status': False
    }
    questions = Question.objects.filter(questionnaire=qid).order_by('id')

    if request.method == "POST":
        try:
            responses = {q: None for q in questions}

            # Validate every question is answered
            for question in questions:
                answer = request.POST.get(str(question.id), None)
                if answer == '' or answer is None:
                    if not (qid == '1' and question.id > 8):
                        raise Exception(question.question_order)
                else:
                    responses[question] = answer

            # check questionnaire 1: 9, 10, 11 questions should only has one 
            # answer. 
            if qid == '1':
                extra_q = []
                for q, a in responses.iteritems():
                    if q.question_order > 8:
                        extra_q.append(a is not None)
                if not any(extra_q) or extra_q.count(True) > 1:
                    raise Exception(9)

            # Save every question. 
            for question, answer in responses.iteritems():
                if answer is None:
                    continue
                answer = Answer(question=question,
                                submit_date=submit_date,
                                patient_id=patient_id,
                                response=answer,
                                note="")
                answer.save()
            context['status'] = True
        except IntegrityError as e:
            context['error_msg'] = e.message
        except Exception as err:
            context['error_msg'] = 'Question #{} is incomplete'.format(
                err.args[0])

    else:
        context['error_msg'] = 'Form is invalid.'

    return render(request, template, context)


def aboutView(request):
    return render(request, 'questionnaire/about.html', {})

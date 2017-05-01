from django.http import HttpResponse
from django.shortcuts import render
from .search_forms import ResponseForm
from django.db import connection
from questionnaire.models import *
import json


def db_execute(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def generate_query(form):
    where_conditions = []
    if form['questionnaire_id']:
        where_conditions.append(
            "question.questionnaire_id = {}".format(form['questionnaire_id']))
    if form['patient_id']:
        where_conditions.append(
            "patient_id = {}".format(form['patient_id'])
        )
    # DateTime

    where_stm = ""
    if len(where_conditions):
        where_stm = "WHERE " + " AND ".join(where_conditions)

    query = """
        SELECT patient_id, submit_date, 
            GROUP_CONCAT(option.option_order) as answers, 
            SUM(option.score)
        FROM answer 
          JOIN question ON answer.question_id = question.id
          JOIN option ON answer.response = option.id
        {}
        GROUP BY question.questionnaire_id, patient_id, submit_date
    """.format(where_stm)
    return query


def index(request):
    context = {'form': None, 'table': {}}
    if request.method == "POST":
        form = ResponseForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form_data = form.cleaned_data
            query = generate_query(form_data)

            data = []
            for row in db_execute(query):
                row = map(str, row)
                data.append(row[:2] + row[2].split(',') + [row[3]])

            question_count = Question.objects.filter(
                questionnaire=form_data['questionnaire_id']).count()
            title = ['Patient id', 'Submit date'] + map(str, range(1, question_count + 1)) + [
                'Total Score']
            context['table'] = {
                'columns': title,
                'data': json.dumps(data)
            }
    else:
        context['form'] = ResponseForm()

    return render(request, 'response/index.html', context)

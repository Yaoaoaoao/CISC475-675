from django.http import HttpResponse
from django.shortcuts import render
from .search_forms import ResponseForm
from django.db import connection
from questionnaire.models import *


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
        SELECT patient_id, GROUP_CONCAT(response) as answers, SUM(option.score)
        FROM answer 
          JOIN question ON answer.question_id = question.id
          JOIN option ON answer.response = option.id
        {}
        GROUP BY question.questionnaire_id, patient_id, submit_date
    """.format(where_stm)
    return query


def index(request):
    context = {}
    if request.method == "POST":
        form = ResponseForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form_data = form.cleaned_data
            context['form_data'] = form_data
            query = generate_query(form_data)
            context['data'] = db_execute(query)
    else:
        context['form'] = ResponseForm()

    return render(request, 'response/index.html', context)

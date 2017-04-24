from django.http import HttpResponse
from django.shortcuts import render
from .search_forms import ResponseForm
from django.db import connection

def db_execute(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def generate_query(form):
    questionnaire, patient_id, date_from, date_to = form
    query = """
        SELECT patient_id, GROUP_CONCAT(response) as answers, SUM(option.score)
        FROM answer 
          JOIN question ON answer.question_id = question.id
          JOIN questionnaire ON question.questionnaire_id = questionnaire.id
          JOIN option ON answer.response = option.id
        GROUP BY questionnaire.id, patient_id, submit_date
    """
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

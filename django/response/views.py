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
    query = ""
    return query


def index(request):
    context = {}
    if request.method == "POST":
        form = ResponseForm(request.POST)
        context['form'] = form
        if form.is_valid():
            query = generate_query(form.cleaned_data)
            context['data'] = db_execute(query)
    else:
        context['form'] = ResponseForm()

    return render(request, 'response/index.html', context)

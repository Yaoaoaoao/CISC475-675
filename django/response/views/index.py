from django.shortcuts import render
from .utils import *
from response.search_forms import ResponseForm
from questionnaire.models import *
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
import json


@user_passes_test(lambda u: u.is_superuser,
                  login_url=reverse_lazy('questionnaire:login'))
def index(request):
    context = {'form': None, 'table': {}}
    if request.method == "POST":
        form = ResponseForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form_data = form.cleaned_data
            question_count = Question.objects.filter(
                questionnaire=form_data['questionnaire_id']).count()
            question_title = map(str, range(1, question_count + 1))
            title = ['Patient id', 'Submit date'] + question_title + [
                'Total Score']

            data = []
            query = generate_query(form_data)
            for record in db_execute(query):
                responses = {str(i): '' for i in range(1, question_count + 1)}
                for col in record[2].split(','):
                    idx, response = col.split('-')
                    responses[idx] = response

                # sorted patient response by key
                row = [responses[k] for k in sorted(responses, key=int)]
                data.append(map(str, record[:2]) + row + [record[3]])

            context['table'] = {
                'columns': title,
                'data': json.dumps(data)
            }
    else:
        context['form'] = ResponseForm()

    return render(request, 'response/index.html', context)

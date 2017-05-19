from django.shortcuts import render
from .utils import *
from response.search_forms import TrackForm
from questionnaire.models import *
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
import json


def track_data_format(data):
    """ Reformat database result to Google Chart format. 
    Args: 
        data (list): [[patient_id, submit_date, responses_string, total_score]]
    Returns: 
        Google Chart Data Table Format in json format
        https://developers.google.com/chart/interactive/docs/reference#DataTable
        First column: Date
        Second column: total_score
    """

    columns = [{"label": 'Date', "type": "string"},
               {"label": 'Severity Score', "type": "number"}]
    rows = []
    for line in data:
        rows.append({"c": [{"v": str(line[1])},
                           {"v": int(line[3])}
                           ]})

    return json.dumps({"cols": columns, "rows": rows})


@user_passes_test(lambda u: u.is_superuser,
                  login_url=reverse_lazy('questionnaire:login'))
def trackView(request):
    context = {'form': None, 'data': {}, 'error': None}
    if request.method == "POST":
        form = TrackForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form_data = form.cleaned_data
            if form_data['patient_id'] is None:
                context['form'] = TrackForm()
                context['error'] = "Patient id is required."
            else:
                # Get data from every questionnaire
                for qid in [1, 2]:
                    form_data['questionnaire_id'] = qid
                    query = generate_query(form_data)
                    context['data'][qid] = {
                        'title': str(Questionnaire.objects.get(id=qid).title),
                        'data': track_data_format(db_execute(query))
                    }
    else:
        context['form'] = TrackForm()

    return render(request, 'response/track.html', context)

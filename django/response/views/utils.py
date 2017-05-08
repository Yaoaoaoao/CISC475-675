from django.db import connection

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
            GROUP_CONCAT(question.question_order || '-' || option.option_order) as answers, 
            SUM(option.score)
        FROM answer 
          JOIN question ON answer.question_id = question.id
          JOIN option ON answer.response = option.id
        {}
        GROUP BY question.questionnaire_id, patient_id, submit_date
        ORDER BY submit_date
    """.format(where_stm)
    return query


from django.test import TestCase
from django.urls import reverse
from .models import *


class QuestionnaireTests(TestCase):
    QUESTIONNAIRE_ID = 1
    QUESTIONNAIRE_TITLE = 'Test Questionnaire'
    PATIENT_ID = 100

    def setUp(self):
        q = Questionnaire.objects.create(id=self.QUESTIONNAIRE_ID,
                                         title=self.QUESTIONNAIRE_TITLE)
        q.save()

    def test_questionnaire_view(self):
        """
        """
        url = reverse('questionnaire:view',
                      args=(self.QUESTIONNAIRE_ID, self.PATIENT_ID))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.QUESTIONNAIRE_TITLE)


    def test_submit_patient_response(self):
        """
        """
        url = reverse('questionnaire:submit',
                      args=(self.QUESTIONNAIRE_ID, self.PATIENT_ID))
        response = self.client.post(url, {'1': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Upload successfully')


    def test_submit_empty_response(self):
        """
        """
        url = reverse('questionnaire:submit',
                      args=(self.QUESTIONNAIRE_ID, self.PATIENT_ID))
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Fail')
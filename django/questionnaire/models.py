from django.db import models
import django
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)  
    desc = models.CharField(max_length=200)  

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey('Question', default=None)
    answer_text = models.CharField(max_length=200)
    questionnaire = models.ForeignKey('Questionnaire', default=None, null=True)

    def __str__(self):
        return "%s, %s, %s" % (self.question.id, self.answer_text, self.questionnaire)

class Questionnaire(models.Model):
    patient = models.ForeignKey('Patient', default=None, null=True)
    date = models.DateTimeField('Time completed', default=django.utils.timezone.now())

    def __str__(self):
        return "Patient subject: %s, Submission: %s" % (self.patient, self.date.date())


class Patient(models.Model):
    subject_code = models.IntegerField(default=0, null=True)

    def __str__(self):
        return 'Subject: ' + str(self.subject_code)

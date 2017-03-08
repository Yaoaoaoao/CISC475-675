# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals


from django.db import models

class Questionnaire(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return str(self.id) + ". " + self.title

    class Meta:
        managed = False
        db_table = 'questionnaire'

class Question(models.Model):

    QUESTION_TYPES = (('SC', 'Scale'), ('SIN', 'Single Choice'))
    id = models.AutoField(primary_key=True)  # AutoField?
    questionnaire = models.ForeignKey(Questionnaire)
    #question_id = models.IntegerField()
    question_order = models.IntegerField()
    question_text = models.TextField()
    question_type = models.CharField(max_length=25, choices=QUESTION_TYPES, default='SIN')

    def __str__(self):
        return str(self.id) + ". " + self.question_text

    class Meta:
        managed = False
        db_table = 'question'

class Option(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    question = models.ForeignKey(Question)
    option_order = models.IntegerField()
    option_text = models.TextField()
    score = models.IntegerField()

    def __str__(self):
        return str(self.question.id) + "." + str(self.option_order) + " " + self.option_text + "  " + str(self.score)

    class Meta:
        managed = False
        db_table = 'option'

class Answer(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    question = models.ForeignKey(Question)
    patient_id = models.IntegerField()
    submit_date = models.DateField()
    response = models.TextField()
    note = models.TextField()

    def __str__(self):
        return self.id

    class Meta:
        managed = False
        db_table = 'answer'

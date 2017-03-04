# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Answer(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    question_id = models.IntegerField()
    patient_id = models.IntegerField()
    submit_date = models.DateField()
    response = models.TextField()
    note = models.TextField()

    class Meta:
        managed = False
        db_table = 'answer'


class Option(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    question_id = models.IntegerField()
    option_order = models.IntegerField()
    option_text = models.TextField()
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'option'


class Question(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    questionnaire_id = models.IntegerField()
    question_order = models.IntegerField()
    question_text = models.TextField()
    question_type = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'question'


class Questionnaire(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'questionnaire'

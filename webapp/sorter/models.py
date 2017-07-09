# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import BooleanField


class SortedIdols(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    bust = models.IntegerField()
    waist = models.IntegerField()
    hip = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    cute = models.IntegerField()
    cool = models.IntegerField()
    passion = models.IntegerField()
    pictures = models.CharField(max_length=256)
    
class SuggestedIdols(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    bust = models.IntegerField()
    waist = models.IntegerField()
    hip = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    cute = models.IntegerField()
    cool = models.IntegerField()
    passion = models.IntegerField()
    pictures = models.CharField(max_length=256)

   
class MergeSortChoices(models.Model):
    id = models.AutoField(primary_key=True)
    shuffled_idols = ArrayField(models.IntegerField(),null=True)
    choices = ArrayField(models.IntegerField(),null=True)
    mergesort_ans = ArrayField(models.IntegerField(),null=True)
    finish_mergesort = BooleanField(default=False)
    suggest_score = ArrayField(models.FloatField(),null=True)
    pref_coefficient = ArrayField(models.CharField(max_length=10),null=True)
    most_preferred_name = models.CharField(max_length=30,null=True)
    most_preferred_picture = models.CharField(max_length=256,null=True)    
    timestamp = models.DateTimeField(auto_now=True)
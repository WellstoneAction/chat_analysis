from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import calendar
import datetime

from django.db import models

class Series(models.Model):
    title = models.CharField(max_length = 150, null = True, blank = True)
    partner = models.CharField(max_length = 45, default = "Wellstone Action")
    start_date = models.DateField(null = True, blank = True)
    end_date = models.DateField(null = True, blank = True)

    def __unicode__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    number = models.CharField(max_length = 3, null = True, blank=True)
    start_date = models.DateField(null = True, blank = True)
    end_date = models.DateField(null = True, blank = True)  
    series = models.ForeignKey(Series)


class Training(models.Model):
    training_id = models.CharField(max_length = 3, null = True, blank = True)
    dateandtime = models.DateTimeField(null = True, blank = True)
    weekday = models.CharField(max_length = 10, null=True, blank=True)
    lesson = models.ForeignKey(Lesson)
    
    def __unicode__(self):
        return "Training "+ self.lesson.number+ ", "+self.weekday


class Person(models.Model):
    screen_name = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=170, null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    longitude = models.FloatField(default = -93.2650)
    latitude = models.FloatField(default = 44.9778)
    first_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45, null=True, blank=True)
    role = models.IntegerField(default = 1)# (1 = student, 2 = trainer, 3 = coach, 4 = other_staff, 5 = observer)

    def __unicode__(self):
        return self.screen_name


class Message(models.Model):
    id_str = models.CharField(max_length = 150, null=True, blank=True)
    author = models.ForeignKey(Person)
    text = models.TextField(null=True, blank=True)
    time_sent = models.DateTimeField(null=True, blank=True)
    training = models.ForeignKey(Training)

    def __unicode__(self):
        return self.person.screen_name + self.id_str

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from app.models import *
import calendar
from datetime import date


def index(request):
    series = Series.objects.all()
    people_count = Person.objects.count()
    messages_count = Message.objects.count()
    trainings_count = Training.objects.count()
    series_count = Series.objects.count()
    return render(request, "index.html", {'series' : series, 'people_count' : people_count,'messages_count' : messages_count, 'trainings_count' : trainings_count, 'series_count': series_count})

def trainings(request):
    trainings = Training.objects.all()
    people_count = Person.objects.count()
    messages_count = Message.objects.count()
    trainings_count = Training.objects.count()
    series_count = Series.objects.count()
    return render(request, "trainings.html", {'trainings' : trainings, 'people_count' : people_count,'messages_count' : messages_count, 'trainings_count' : trainings_count, 'series_count': series_count})


def lessons(request):
    lessons = Lesson.objects.all()
    people_count = Person.objects.count()
    messages_count = Message.objects.count()
    trainings_count = Training.objects.count()
    series_count = Series.objects.count()
    return render(request, "lessons.html", {'lessons' : lessons, 'people_count' : people_count,'messages_count' : messages_count, 'trainings_count' : trainings_count, 'series_count': series_count})


def participants(request):
    people = Person.objects.all().order_by('screen_name')
    people_count = Person.objects.count()
    messages_count = Message.objects.count()
    trainings_count = Training.objects.count()
    series_count = Series.objects.count()
    return render(request, "participants.html", {'people' : people, 'people_count' : people_count,'messages_count' : messages_count, 'trainings_count' : trainings_count, 'series_count': series_count})


def messages(request):
    messages = Message.objects.all()
    people_count = Person.objects.count()
    messages_count = Message.objects.count()
    trainings_count = Training.objects.count()
    series_count = Series.objects.count()
    return render(request, "messages.html", {'messages' : messages, 'people_count' : people_count,'messages_count' : messages_count, 'trainings_count' : trainings_count, 'series_count': series_count})
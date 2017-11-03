from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from app.models import *
import calendar
from datetime import date


def index(request):
    people = Person.objects.all().order_by('screen_name')
    people_count = Person.objects.count()
    messages_count = Message.objects.count()
    trainings_count = Training.objects.count()
    series_count = Series.objects.count()
    return render(request, "index.html", {'people' : people, 'people_count' : people_count,'messages_count' : messages_count, 'trainings_count' : trainings_count, 'series_count': series_count})

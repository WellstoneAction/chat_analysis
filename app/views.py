from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from geopy.geocoders import GoogleV3
from app.models import *
from app.forms import SearchForm
import calendar
from datetime import date


def index(request):
    alumni = Alumnus.objects.all().order_by('twitter_id')
    tweets_count = Tweet.objects.count()
    alumni_count = Alumnus.objects.count()
    trainings_count = Training.objects.count()
    if request.method == "POST":
        form = CallTimeForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get("search_term")
            tweets = Tweet.objects.filter(text__icontains=search_term).all() # icontains is case insensitive            
    else:
        form = SearchForm()
    form = SearchForm()
    return render(request, "index.html", {'alumni' : alumni, 'tweets_count' : tweets_count,'alumni_count' : alumni_count, 'trainings_count' : trainings_count, 'form': form})


def results(request, search_term):
    tweets_count = Tweet.objects.count()
    alumni_count = Alumnus.objects.count()
    trainings_count = Training.objects.count()
    tweets = Tweet.objects.filter(text__icontains=search_term).all() # icontains is case insensitive
    if request.method == "POST":
        form = CallTimeForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get("search_term")
            tweets = Tweet.objects.filter(text__icontains=search_term).all() # icontains is case insensitive
    else:
        form = SearchForm()
    return render(request, "results.html", {'tweets': tweets, 'tweets_count' : tweets_count,'alumni_count' : alumni_count, 'trainings_count' : trainings_count, 'form':form, 'search_term': search_term})
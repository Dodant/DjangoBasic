from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate, Poll, Choice

import datetime

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'elections/index.html', context)

def areas(request, area):
    today = datetime.datetime.now()
    try:
        poll = Poll.objects.get(area = area, start_date__lte = today, end_date__gte=today)
    except:
        poll = None
        candidate = None

    candidates = Candidate.objects.filter(area = area)
    context = {'candidates':candidates, 'area':area, 'poll':poll}
    return render(request, 'elections/area.html', context)
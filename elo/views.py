from django.shortcuts import render
from os import path
import sys
from .python_elo import database_reader

scores = database_reader.pull_all_elo('test')


entries = sorted([dict(zip(("name", "elo"), values)) for values in scores], key=lambda i: i['elo'], reverse=True)


def home(request):
    context = {
        'entries': entries,
    }
    return render(request, 'elo/elo.html', context)


def about(request):
    return render(request, 'elo/about.html')

from django.shortcuts import render
from os import path
import sys
from .python_elo import database_reader, main
from .models import EloForm
from django.http import HttpResponse
from .config import GAME


def home(request):
    scores = database_reader.pull_all_elo('test')
    entries = sorted([dict(zip(("name", "elo"), values)) for values in scores], key=lambda i: i['elo'], reverse=True)

    context = {
        'entries': entries,
    }
    return render(request, 'elo/elo.html', context)


def submit(request):
    form = EloForm()
    return render(request, 'elo/submit.html', {'form':form})


def submission(request):
    info = request.POST
    user_one_name = info['user_one_name']
    user_one_score = info['user_one_score']
    user_two_name = info['user_two_name']
    user_two_score = info['user_two_score']
    main.process_result_from_variables(GAME, user_one_name, user_two_name, user_one_score, user_two_score)
    return HttpResponse('<h1>Submitted</h1>')

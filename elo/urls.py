from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='elo-leaderboard'),
    path('submit/', views.submit, name='elo-submit'),
    path('submit/submit', views.submission, name='elo-submission'),
]

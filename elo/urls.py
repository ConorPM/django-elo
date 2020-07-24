from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='elo-leaderboard'),
    path('about/', views.about, name='elo-about'),

]

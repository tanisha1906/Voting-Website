from django.contrib import admin
from django.urls import include,path
from VotingResult import views

app_name = 'votingresult'
urlpatterns = [
    path('', views.result, name='result'),
    path('result/', views.result, name='result'),
]
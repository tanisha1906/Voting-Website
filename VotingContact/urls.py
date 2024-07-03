from django.contrib import admin
from django.urls import include,path
from VotingContact import views


app_name = 'votingcontact'
urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
]
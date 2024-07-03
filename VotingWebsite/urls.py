from django.contrib import admin
from django.urls import include,path
from VotingWebsite import views

app_name = 'votingwebsite'
urlpatterns = [
    path('', views.website, name='website'),
#     path('website/', views.website, name='website'),
]


from django.contrib import admin
from django.urls import include,path
from VotingHome import views

app_name = 'votinghome'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login-signup/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
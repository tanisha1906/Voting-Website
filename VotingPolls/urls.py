
# urls.py
from django.urls import path
from . import views

app_name = 'votingpolls'
urlpatterns = [
    path('', views.index, name='index'),
    # path('polls/', views.polls, name='polls'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('all_results/', views.all_results, name='all_results'),
]


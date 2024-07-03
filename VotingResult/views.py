from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def result(request):
    # return HttpResponse("This is my Voting Result Page!")
    return render(request,'pages/result.html')
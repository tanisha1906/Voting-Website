from django.shortcuts import render

def website(request):
    context = {
        'user':request.user
    }
    return render(request, 'pages/website.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, "Your message has been submitted successfully!")
        return redirect('votingcontact:contact') 
    else:
        return render(request, 'pages/contact.html')  # Render the contact form template for GET requests

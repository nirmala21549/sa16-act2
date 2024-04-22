# Defines Django views for rendering HTML templates
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def work(request):
    return render(request, 'work.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from django.http import HttpResponse

def say_hey(request):
    return HttpResponse("Hey!")

def say_hey_templates(request):
    return render(request, 'hi.html', {'name': 'Leo'})

# Create your views here.

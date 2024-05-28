from django.shortcuts import render
from django.http import HttpResponse

def say_hey(request):
    return HttpResponse("Hey!")

# Create your views here.

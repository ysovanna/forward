from django.shortcuts import render

# Create your views here.
# testing/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')

def hello(request):
    return HttpResponse('<h1>  Hello, World!</h1>')


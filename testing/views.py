from django.shortcuts import render

# Create your views here.
# testing/views.py
from django.http import HttpResponse

def home(request):
    return render(request,'testing/home.html')

def about(request):
    return HttpResponse('<h1>About</h1>')

def hello(request):
    return HttpResponse('<h1>  Hello, World!</h1>')


# pages/urls.py
from testing.views import home
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='testing-home'),
    path('home/', views.home, name='testing-home'),
    path('about/', views.about, name='testing-about'),
    path('hello/', views.hello, name='testing-hello'),
]
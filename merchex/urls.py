# ~/projects/django-web-app/merchex/merchex/urls.py
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
   path('home', views.home, name='home')

]

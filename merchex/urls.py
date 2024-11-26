# ~/projects/django-web-app/merchex/merchex/urls.py
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('statistic_1', views.statistic_1, name='statistic_1'),
    path('statistic_2', views.statistic_2, name='statistic_2'),
    path('statistic_3', views.statistic_3, name='statistic_3'),
    path('statistic_4', views.statistic_4, name='statistic_4'),
    path('statistic_5/<int:id_employee>', views.statistic_5, name='statistic_5'),
    #path('cluster', views.index, name='index'),
    path('predict/', views.prediction_view, name='predict')
]

# ~/projects/django-web-app/merchex/merchex/urls.py
from django.contrib import admin
from django.urls import path
from listings import views
from django.urls import path


urlpatterns = [
   path('home/', views.home, name='home'),
   path('signup/', views.signup, name='signup'),
   path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:id>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('professors/', views.ProfessorListView.as_view(), name='professor_list'),
    path('professors/<int:id>/', views.ProfessorDetailView.as_view(), name='professor_detail'),
    path('login/', views.login_view, name='login'),  # Map the login view to '/login/'
    path('admin_profile/', views.admin_profile_view, name='admin_profile'),
    path('professor_profile/', views.professor_profile_view, name='professor_profile'),
    path('professor/<int:id>/profile/', views.professor_profile_view, name='professor_profile'),
    path('professor/<int:id>/courses/', views.professor_courses_view, name='professor_courses'),
    path('professor/<int:professor_id>/courses/<int:course_id>/', views.professor_course_detail_view, name='professor_course_detail'),

    
]

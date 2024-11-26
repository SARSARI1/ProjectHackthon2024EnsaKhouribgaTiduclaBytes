# ~/projects/django-web-app/merchex/listings/views.py
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


from django.core.files.storage import default_storage
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from io import BytesIO
import pandas as pd
from datetime import datetime
from collections import defaultdict
from datetime import datetime
from openpyxl import Workbook

from dateutil.relativedelta import relativedelta
from reportlab.lib.pagesizes import A4




# login views

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'listings/homePage.html')

def signup(request):
    return render(request, 'listings/signup.html')

def dashboard(request):
    return render(request, 'listings/dashboard.html')




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
import json
from .models import AdminProfile, Course, Professor

@method_decorator(csrf_exempt, name='dispatch')
class CourseListView(View):
    def get(self, request):
        """Get all courses."""
        courses = list(Course.objects.values())
        return JsonResponse(courses, safe=False)

    def post(self, request):
        """Create a new course."""
        try:
            data = json.loads(request.body)
            course = Course.objects.create(
                title=data.get('title'),
                department_id=data.get('department'),
                is_completed=data.get('is_completed', False),
                course_manager_email=data.get('course_manager_email'),
                client_company_name=data.get('client_company_name'),
                contract_number=data.get('contract_number'),
                invoice_status=data.get('invoice_status'),
                contract_start_date=data.get('contract_start_date'),
                approval_status=data.get('approval_status'),
            )
            return JsonResponse({"id": course.id, "message": "Course created successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class CourseDetailView(View):
    def get(self, request, id):
        """Get a course by ID."""
        try:
            course = Course.objects.values().get(id=id)
            return JsonResponse(course, safe=False)
        except Course.DoesNotExist:
            return JsonResponse({"error": "Course not found"}, status=404)

    def put(self, request, id):
        """Update a course by ID."""
        try:
            data = json.loads(request.body)
            course = Course.objects.get(id=id)
            course.title = data.get('title', course.title)
            course.department_id = data.get('department', course.department_id)
            course.is_completed = data.get('is_completed', course.is_completed)
            course.course_manager_email = data.get('course_manager_email', course.course_manager_email)
            course.client_company_name = data.get('client_company_name', course.client_company_name)
            course.contract_number = data.get('contract_number', course.contract_number)
            course.invoice_status = data.get('invoice_status', course.invoice_status)
            course.contract_start_date = data.get('contract_start_date', course.contract_start_date)
            course.approval_status = data.get('approval_status', course.approval_status)
            course.save()
            return JsonResponse({"message": "Course updated successfully"})
        except Course.DoesNotExist:
            return JsonResponse({"error": "Course not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, id):
        """Delete a course by ID."""
        try:
            course = Course.objects.get(id=id)
            course.delete()
            return JsonResponse({"message": "Course deleted successfully"})
        except Course.DoesNotExist:
            return JsonResponse({"error": "Course not found"}, status=404)



@method_decorator(csrf_exempt, name='dispatch')
class ProfessorListView(View):
    def get(self, request):
        """Get all professors."""
        professors = list(Professor.objects.values())
        return JsonResponse(professors, safe=False)

    def post(self, request):
        """Create a new professor."""
        try:
            data = json.loads(request.body)
            professor = Professor.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                hire_date=data.get('hire_date'),
                is_active=data.get('is_active', True),
                password=data.get('password'),
                birth_date=data.get('birth_date'),
                phone_number=data.get('phone_number'),
                salary=data.get('salary'),
                professor_number=data.get('professor_number')
            )
            return JsonResponse({"id": professor.id, "message": "Professor created successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class ProfessorDetailView(View):
    def get(self, request, id):
        """Get a professor by ID."""
        try:
            professor = Professor.objects.values().get(id=id)
            return JsonResponse(professor, safe=False)
        except Professor.DoesNotExist:
            return JsonResponse({"error": "Professor not found"}, status=404)

    def put(self, request, id):
        """Update a professor by ID."""
        try:
            data = json.loads(request.body)
            professor = Professor.objects.get(id=id)
            professor.first_name = data.get('first_name', professor.first_name)
            professor.last_name = data.get('last_name', professor.last_name)
            professor.email = data.get('email', professor.email)
            professor.hire_date = data.get('hire_date', professor.hire_date)
            professor.is_active = data.get('is_active', professor.is_active)
            professor.password = data.get('password', professor.password)
            professor.birth_date = data.get('birth_date', professor.birth_date)
            professor.phone_number = data.get('phone_number', professor.phone_number)
            professor.salary = data.get('salary', professor.salary)
            professor.professor_number = data.get('professor_number', professor.professor_number)
            professor.save()
            return JsonResponse({"message": "Professor updated successfully"})
        except Professor.DoesNotExist:
            return JsonResponse({"error": "Professor not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, id):
        """Delete a professor by ID."""
        try:
            professor = Professor.objects.get(id=id)
            professor.delete()
            return JsonResponse({"message": "Professor deleted successfully"})
        except Professor.DoesNotExist:
            return JsonResponse({"error": "Professor not found"}, status=404)
        
    
    
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminProfile, Professor
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Get 'next' URL from the query parameter or form data
        next_url = request.POST.get('next', request.GET.get('next', '/admin_profile/'))  # Default for admin profile

        # Validate inputs
        if not email or not password:
            messages.error(request, "Email and password are required.")
            return render(request, 'listings/login.html')

        # Admin login (unchanged)
        try:
            admin = AdminProfile.objects.get(email=email)
            if admin.password == password:
                request.session['user_role'] = 'admin'
                request.session['user_email'] = email
                logger.info(f"Admin {email} logged in.")
                return HttpResponseRedirect(next_url)
            else:
                messages.error(request, "Incorrect password for Admin.")
                return render(request, 'listings/login.html')
        except AdminProfile.DoesNotExist:
            pass

@login_required
def admin_profile_view(request):
    if request.session.get('user_role') != 'admin':
        logger.warning("Unauthorized access attempt to Admin Profile.")
        return redirect('login')

    try:
        admin = AdminProfile.objects.get(email=request.session.get('user_email'))
        logger.info(f"Admin profile loaded for {admin.email}.")
    except AdminProfile.DoesNotExist:
        messages.error(request, "Admin not found.")
        return redirect('login')

    return render(request, 'listings/admin_profile.html', {'admin': admin})@login_required
def admin_profile_view(request):
    if request.session.get('user_role') != 'admin':
        logger.warning("Unauthorized access attempt to Admin Profile.")
        return redirect('login')

    try:
        admin = AdminProfile.objects.get(email=request.session.get('user_email'))
        logger.info(f"Admin profile loaded for {admin.email}.")
    except AdminProfile.DoesNotExist:
        messages.error(request, "Admin not found.")
        return redirect('login')

    return render(request, 'listings/admin_profile.html', {'admin': admin})



from django.shortcuts import render, get_object_or_404
from .models import Professor

def professor_profile_view(request, id):
    # Fetch professor by ID
    professor = get_object_or_404(Professor, id=id)

    return render(request, 'listings/professor_profile.html', {'professor': professor})



from .models import Course

def professor_courses_view(request, id):
    # Fetch professor by ID
    professor = get_object_or_404(Professor, id=id)

    # Get all courses assigned to this professor
    courses = professor.courseprofessor_set.all()  # Assuming a relationship exists

    return render(request, 'listings/professor_courses.html', {'professor': professor, 'courses': courses})

def professor_course_detail_view(request, professor_id, course_id):
    # Fetch professor by ID
    professor = get_object_or_404(Professor, id=professor_id)

    # Fetch specific course by course ID
    course = get_object_or_404(professor.courseprofessor_set, id=course_id)

    return render(request, 'listings/professor_course_detail.html', {'professor': professor, 'course': course})







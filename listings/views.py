# ~/projects/django-web-app/merchex/listings/views.py
from django.contrib import messages
from django.http import HttpResponse
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
    return render(request, 'listings/agentsCrud.html')

from django.shortcuts import render
from django.db.models import Count
from .models import Course, Professor, Department, RequiredSkill, GainedSkill
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Count, Sum, F
from django.db.models.functions import TruncYear
from .models import Course, Professor, Department, RequiredSkill, GainedSkill
from datetime import datetime

def home(request):
    return render(request, 'listings/agentsCrud.html')
from django.db.models import Count, F
from django.db.models.functions import TruncYear
from .models import Course, Professor, Department, RequiredSkill, GainedSkill
from datetime import datetime

from django.shortcuts import render
from django.db.models import Count, Sum
from django.db.models.functions import TruncYear
from .models import Course, Department, RequiredSkill, GainedSkill, Professor, CourseProfessor
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, F
from django.db.models.functions import TruncYear
from .models import Course, Professor, Department, RequiredSkill, GainedSkill, CourseRequiredSkill  # Add CourseRequiredSkill here
from datetime import datetime
from .models import Course, Professor, Department, RequiredSkill, GainedSkill, CourseGainedSkill, CourseRequiredSkill, CourseProfessor

def dashboard(request):
    # 1. Calculate course completion rate by department
    total_courses = Course.objects.count()
    completed_courses = Course.objects.filter(is_completed=True).count()
    completion_rate = (completed_courses / total_courses * 100) if total_courses else 0
    
    # 2. Counting required and gained skills
    skills_comparison = {
        "required": RequiredSkill.objects.count(),
        "gained": GainedSkill.objects.count(),
    }
    
    # 3. Counting the number of courses offered by each department
    courses_by_department_data = {
        "labels": list(Department.objects.values_list('name', flat=True)),
        "counts": list(Course.objects.values('department')
                       .annotate(total=Count('id'))
                       .values_list('total', flat=True))
    }
    
    # 4. The number of courses offered by each department, broken down by year (contract start date)
    courses_by_year_data = {
        "years": list(Course.objects.annotate(year=TruncYear('contract_start_date'))
                      .values('year')
                      .distinct()
                      .order_by('year')
                      .values_list('year', flat=True)),
        "counts": list(Course.objects.annotate(year=TruncYear('contract_start_date'))
                      .values('year')
                      .annotate(total=Count('id'))
                      .order_by('year')
                      .values_list('total', flat=True)),
    }

    # 5. Compare the number of required skills vs. gained skills for each course
    course_skills_comparison = []
    courses = Course.objects.all()
    for course in courses:
        required_skills = CourseRequiredSkill.objects.filter(course=course).count()
        gained_skills = CourseGainedSkill.objects.filter(course=course).count()
        course_skills_comparison.append({
            "course_title": course.title,
            "required_skills": required_skills,
            "gained_skills": gained_skills
        })
    
    # 6. Count the total number of days each professor worked
    professor_working_days = []
    professors = Professor.objects.all()
    for professor in professors:
        assigned_courses = CourseProfessor.objects.filter(professor=professor).values('assignment_date').distinct()
        working_days = len(assigned_courses)  # Count distinct assignment dates
        professor_working_days.append({
            "professor_name": f"{professor.first_name} {professor.last_name}",
            "working_days": working_days
        })
    
    # Send context to the template
    context = {
        "completion_rate": completion_rate,
        "total_courses": total_courses,
        "skills_comparison": skills_comparison,
        "courses_by_department_data": courses_by_department_data,
        "courses_by_year_data": courses_by_year_data,
        "course_skills_comparison": course_skills_comparison,
        "professor_working_days": professor_working_days
    }
    
    return render(request, 'listings/dashboard.html', context)

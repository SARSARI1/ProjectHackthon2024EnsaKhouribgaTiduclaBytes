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
from django.db.models import Count
from django.db.models.functions import TruncYear
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
    
    # 7. Count the total number of departments, professors
    total_departments = Department.objects.count()
    total_professors = Professor.objects.count()
    

    # Send context to the template
    context = {
        "completion_rate": completion_rate,
        "total_courses": total_courses,
        "skills_comparison": skills_comparison,
        "courses_by_department_data": courses_by_department_data,
        "courses_by_year_data": courses_by_year_data,
        "course_skills_comparison": course_skills_comparison,
        "professor_working_days": professor_working_days,
        "total_departments": total_departments,
        "total_professors": total_professors
    }
    
    return render(request, 'listings/dashboard.html', context)


from django.http import JsonResponse
from django.db.models import Count, F
from django.db.models.functions import TruncMonth, TruncYear
from .models import Course, Department, CourseRequiredSkill, CourseGainedSkill, CourseProfessor, Professor

# Statistic 1: Visualize the completion rate of courses by department
def statistic_1(request):
    departments = Department.objects.all()
    completion_rates = []
    for department in departments:
        total_courses = Course.objects.filter(department=department).count()
        completed_courses = Course.objects.filter(department=department, is_completed=True).count()
        completion_rate = (completed_courses / total_courses * 100) if total_courses else 0
        completion_rates.append({
            "department": department.name,
            "completion_rate": completion_rate
        })
    return JsonResponse({"completion_rates": completion_rates})


# Statistic 2: Number of courses offered by each department
def statistic_2(request):
    data = Course.objects.values(department_name=F('department__name')).annotate(course_count=Count('id'))
    return JsonResponse({"courses_by_department": list(data)})


# Statistic 3: Compare the number of required skills vs. gained skills for each course
def statistic_3(request):
    data = []
    courses = Course.objects.all()
    for course in courses:
        required_skills = CourseRequiredSkill.objects.filter(course=course).count()
        gained_skills = CourseGainedSkill.objects.filter(course=course).count()
        data.append({
            "course_title": course.title,
            "required_skills": required_skills,
            "gained_skills": gained_skills
        })
    return JsonResponse({"course_skills_comparison": data})


# Statistic 4: The number of courses offered by each department, broken down by year or month
def statistic_4(request):
    data = {}
    departments = Department.objects.all()
    for department in departments:
        yearly_data = Course.objects.filter(department=department).annotate(year=TruncYear('contract_start_date')).values('year').annotate(course_count=Count('id'))
        monthly_data = Course.objects.filter(department=department).annotate(month=TruncMonth('contract_start_date')).values('month').annotate(course_count=Count('id'))
        data[department.name] = {
            "yearly": list(yearly_data),
            "monthly": list(monthly_data)
        }
    return JsonResponse({"courses_by_department": data})


# Statistic 5: Counts the total number of days a professor worked
def statistic_5(request, id_employee):
    try:
        professor = Professor.objects.get(id=id_employee)
    except Professor.DoesNotExist:
        return JsonResponse({"error": "Professor not found"}, status=404)
    
    # Calculate unique working days
    unique_working_days = CourseProfessor.objects.filter(professor=professor).values_list('assignment_date', flat=True).distinct()
    working_days_count = len(unique_working_days)

    return JsonResponse({
        "professor_name": f"{professor.first_name} {professor.last_name}",
        "working_days": working_days_count
    })


from django.http import JsonResponse
from rest_framework.decorators import api_view
import numpy as np

# Load pre-trained KMeans model, data, and encoders
# Ensure these are available in your project context
# Example:
# kmeans_model = joblib.load('path_to_saved_model.pkl')
# data = pd.read_csv('path_to_clustered_data.csv')
# encoders = {'col1': LabelEncoder().fit(['value1', 'value2', ...]), ...}

'''@api_view(['POST'])
def predict_missing_fields(request):
    """
    Predict missing fields based on the provided input and clustering model.
    """
    try:
        input_data = request.data  # Get JSON data from the POST request

        # Validate input
        if not isinstance(input_data, dict) or 'CourseTitle' not in input_data:
            return JsonResponse({'error': "Invalid input. 'CourseTitle' is required."}, status=400)

        # Prepare input data for prediction
        input_data_encoded = []
        for col in data.columns[:-1]:  # Exclude the 'Cluster' column
            if col in input_data:  # Field provided
                if col in encoders:  # Encode if categorical
                    input_data_encoded.append(encoders[col].transform([input_data[col]])[0])
                else:  # Use numeric value directly
                    input_data_encoded.append(input_data[col])
            else:  # Missing field: use default value
                if col in encoders:  # Default for categorical columns
                    input_data_encoded.append(0)  # Encoders start with 0
                else:  # Default for numeric columns
                    input_data_encoded.append(data[col].mean())  # Column mean

        # Convert to NumPy array
        input_data_encoded = np.array(input_data_encoded).reshape(1, -1)

        # Predict the cluster
        cluster_label = kmeans_model.predict(input_data_encoded)[0]

        # Extract cluster data and compute means
        cluster_data = data[data['Cluster'] == cluster_label]
        predicted_means = cluster_data.mean()

        # Decode the predicted fields
        predicted_fields = {}
        for col in data.columns[:-1]:  # Exclude 'Cluster'
            if col not in input_data:  # Predict only missing fields
                if col in encoders:  # Decode if categorical
                    decoded_value = encoders[col].inverse_transform([int(round(predicted_means[col]))])[0]
                    predicted_fields[col] = decoded_value
                else:
                    predicted_fields[col] = predicted_means[col]  # Numeric value

        return JsonResponse(predicted_fields, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)'''



import os
import numpy as np
import pandas as pd
import joblib
from django.shortcuts import render
from .forms import PredictionForm
from sklearn.preprocessing import LabelEncoder  # Assurez-vous d'importer LabelEncoder

# Chemin absolu pour le fichier du modèle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'kmeans_model.pkl')

# Vérifier si le fichier du modèle existe avant de le charger
if os.path.exists(model_path):
    kmeans_model = joblib.load(model_path)  # Charger le modèle KMeans
else:
    raise FileNotFoundError(f"Le fichier {model_path} n'a pas été trouvé.")

# Charger les données avec les clusters
data_path = os.path.join(BASE_DIR, 'data_with_clusters.csv')
if os.path.exists(data_path):
    data = pd.read_csv(data_path)  # Charger les données avec les clusters
else:
    raise FileNotFoundError(f"Le fichier de données {data_path} n'a pas été trouvé.")

# Préparer les encodeurs pour les colonnes non numériques
label_encoders = {}  # Dictionnaire pour stocker les encodeurs
non_numeric_columns = data.select_dtypes(include=['object']).columns

for col in non_numeric_columns:
    encoder = LabelEncoder()
    data[col] = encoder.fit_transform(data[col])
    label_encoders[col] = encoder

def predict_fields(input_data):
    # Encoder les données d'entrée
    input_data_encoded = {}
    for col, value in input_data.items():
        if col in label_encoders:
            input_data_encoded[col] = label_encoders[col].transform([value])[0]
        else:
            input_data_encoded[col] = value  # Valeurs numériques

    # Créer un vecteur de caractéristiques pour la prédiction
    feature_vector = []
    for col in data.columns:
        if col in input_data_encoded:
            feature_vector.append(input_data_encoded[col])
        elif col != 'Cluster':
            feature_vector.append(0)  # Valeur par défaut

    # Prédire le cluster
    feature_vector = np.array(feature_vector).reshape(1, -1)
    cluster_label = kmeans_model.predict(feature_vector)[0]

    # Extraire les données pour le cluster prédicté
    cluster_data = data[data['Cluster'] == cluster_label]
    predicted_values = cluster_data.mean()

    # Décoder les valeurs catégorielles
    decoded_predictions = {}
    for col in data.columns:
        if col in input_data:
            decoded_predictions[col] = input_data[col]
        else:
            if col in label_encoders:
                decoded_value = label_encoders[col].inverse_transform([int(round(predicted_values[col]))])[0]
                decoded_predictions[col] = decoded_value
            else:
                decoded_predictions[col] = predicted_values[col]
    return decoded_predictions

def index(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data
            predictions = predict_fields(input_data)
            return render(request, 'index.html', {'form': form, 'predictions': predictions})
    else:
        form = PredictionForm()
    return render(request, 'listings/index.html', {'form': form})




# views.py
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from django.shortcuts import render
from django import forms

# Charger le modèle et les données
kmeans_model = joblib.load('kmeans_model.pkl')  # Remplacez par le chemin réel
data = pd.read_csv(r'C:\Users\oki\OneDrive - Université Sultan Moulay Slimane\projet_ocp_pfa\MyOCP\my_ocp_pfa_projet_final_version\django-web-app\merchex\cleaned_data_hackthone_final.csv')    # Chargez vos données sauvegardées
encoders = {col: LabelEncoder().fit(data[col]) for col in data.select_dtypes(include=['object']).columns}

# Formulaire Django
class PredictionForm(forms.Form):
    CourseTitle = forms.CharField(label='Course Title', max_length=100, required=False)
    RequiredSkill = forms.CharField(label='Required Skill', max_length=100, required=False)
    SchoolDepartment = forms.CharField(label='School Department', max_length=100, required=False)

from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import joblib

# Charger les données et le modèle
data = pd.read_csv(r'C:\Users\oki\OneDrive - Université Sultan Moulay Slimane\projet_ocp_pfa\MyOCP\my_ocp_pfa_projet_final_version\django-web-app\merchex\cleaned_data_hackthone_final.csv')
kmeans_model = joblib.load('kmeans_model.pkl')

# Encoder les colonnes non numériques
non_numeric_columns = data.select_dtypes(include=['object']).columns
encoders = {col: LabelEncoder().fit(data[col]) for col in non_numeric_columns}

def prediction_view(request):
    predictions = None

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Préparer les données d'entrée
            input_data = {field: form.cleaned_data[field] for field in form.fields}

            # Appeler la méthode de prédiction
            predictions = predict_missing_fields(input_data)

    else:
        form = PredictionForm()

    return render(request, 'listings/index.html', {'form': form, 'predictions': predictions})

def predict_missing_fields(input_data):
    """
    Predict the missing fields for a given input based on the nearest cluster.
    
    :param input_data: Dictionary containing the known input columns.
    :return: Dictionary with predicted fields.
    """
    try:
        # Prepare the input columns according to the model
        input_data_encoded = []
        
        # Ensure that we are using the correct columns from the model (exclude 'Cluster')
        for col in data.columns[:-1]:  # Exclude the 'Cluster' column
            if col in input_data:  # If the column is provided
                if col in encoders:  # Encode if categorical
                    input_data_encoded.append(encoders[col].transform([input_data[col]])[0])
                else:  # Directly append if numerical
                    input_data_encoded.append(input_data[col])
            else:  # For missing columns, fill with defaults
                if col in encoders:  # Default value for categorical columns
                    input_data_encoded.append(0)  # Default encoding for categories
                else:  # Default value for numerical columns
                    input_data_encoded.append(data[col].mean())  # Use mean of the column

        # Convert to numpy array and reshape for prediction
        input_data_encoded = np.array(input_data_encoded).reshape(1, -1)

        # Make the prediction using the trained model
        cluster_label = kmeans_model.predict(input_data_encoded)[0]

        # Get the data for the predicted cluster
        cluster_data = data[data['Cluster'] == cluster_label]
        predicted_means = cluster_data.mean()

        # Decode the predicted fields
        predicted_fields = {}
        for col in data.columns[:-1]:  # Exclude 'Cluster' column
            if col not in input_data:  # Predict only the missing fields
                if col in encoders:  # Decode if categorical
                    decoded_value = encoders[col].inverse_transform([int(round(predicted_means[col]))])[0]
                    predicted_fields[col] = decoded_value
                else:
                    predicted_fields[col] = predicted_means[col]  # Numerical value

        return predicted_fields

    except Exception as e:
        return {'error': str(e)}




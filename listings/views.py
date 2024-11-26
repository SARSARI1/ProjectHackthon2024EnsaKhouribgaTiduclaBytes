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

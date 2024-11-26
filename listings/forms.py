# ~/projects/django-web-app/merchex/listings/forms.py
from django import forms

# Formulaire Django avec seulement CourseTitle
class PredictionForm(forms.Form):
    CourseTitle = forms.CharField(label='Course Title', max_length=100, required=True)



    
        


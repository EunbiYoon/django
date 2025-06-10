from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    #dictionary
    students=Student.objects.all()
    return render(request, 'home.html', {'students':students})

def student(request, student_id):
    try: # exist
        student=Student.objects.get(id=student_id)

    except: # non exist
        student=None
    
    return render(request, 'student.html', {'student':student})



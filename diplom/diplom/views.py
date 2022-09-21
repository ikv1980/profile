from django.shortcuts import render
from .models import Education


def home(request):
    return render(request, 'home.html', {'title':'Портфолио Иванова Константина'})

def about(request):
    return render(request, 'about.html', {'title':'Резюме'})

def education(request):
    data = {'educ': Education.objects.all(), 'title':'Сертификаты и дипломы'}
    return render(request, 'education.html', data)

def project(request):
    return render(request, 'project.html', {'title':'Проекты'})
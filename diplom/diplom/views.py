from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'title':'Портфолио Иванова Константина'})

def about(request):
    return render(request, 'about.html', {'title':'Резюме'})

def education(request):
    return render(request, 'education.html', {'title':'Сертификаты и дипломы'})

def project(request):
    return render(request, 'project.html', {'title':'Проекты'})
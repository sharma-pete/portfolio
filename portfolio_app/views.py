from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def info(request):
    return render(request, 'html/info.html')


def view_resume(request):
    return render(request, 'html/resume.html')


def view_projects(request):
    return render(request, 'html/projects.html')


def view_education(request):
    return render(request, 'html/education.html')

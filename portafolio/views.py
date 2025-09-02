from django.shortcuts import render
from .models import projects

# Create your views here.
def portafolio_home(request):
    return render(request, 'home.html')

def portafolio_projects(request):
    filter_project = []
    for project in projects:
        if not project.is_draft():
            filter_project.append(project)
    return render(request, 'projects.html', { 'projects': filter_project })
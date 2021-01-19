from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects' : projects}) 

def details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/details.html', { 'project' : project })

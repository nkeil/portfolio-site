from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Project

class IndexView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'
    
class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/details.html'

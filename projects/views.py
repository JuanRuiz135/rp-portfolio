from django.shortcuts import render
from projects.models import Project
# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'main_page.html', context)

from django.shortcuts import render
from .models import PersonalInfo, Project

def home(request):
    personal_info = PersonalInfo.objects.first()  # Recuperar la primera entrada
    projects = Project.objects.all()  # Recuperar todos los proyectos

    return render(request, 'portfolio/home.html', {  # Asegúrate de que la ruta es correcta
        'personal_info': personal_info,
        'projects': projects,
    })

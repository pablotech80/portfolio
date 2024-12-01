from django.contrib import admin
from .models import PersonalInfo, Project

# Registra los modelos para que aparezcan en el panel de administración
admin.site.register(PersonalInfo)
admin.site.register(Project)

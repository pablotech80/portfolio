from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta principal para la vista "home"
]

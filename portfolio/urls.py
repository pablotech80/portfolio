from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Ruta principal para la vista "home"
]
# Esto es necesario para servir los archivos de media
if settings.DEBUG:  # En desarrollo, Django maneja los archivos automáticamente
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:  # En producción, WhiteNoise manejará los archivos estáticos, pero los de media deben ser gestionados externamente
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
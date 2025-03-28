
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

urlpatterns = [
    path("", lambda request: render(request, "index.html"), name="home"),
]

# Solo habilitar rutas de media y estáticos si DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Servir estáticos
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Servir media




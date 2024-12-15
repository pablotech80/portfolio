#!/bin/bash

# Activar el entorno virtual
source ~ / DjangoProject/.venv/bin/activate

# Ejecutar Gunicorn directamente en el puerto 80
gunicorn DjangoProject.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 3 \
    --error-logfile ~/DjangoProject/logs/gunicorn-error.log \
    --access-logfile ~/DjangoProject/logs/gunicorn-access.log

#!/bin/bash

# Activar el entorno virtual
source ~/DjangoProject/.venv/bin/activate

# Ejecutar Gunicorn con configuración completa y logs
gunicorn DjangoProject.wsgi:application \
    --bind 0.0.0.0:8000 \
    --error-logfile ~/DjangoProject/logs/gunicorn-error.log \
    --access-logfile ~/DjangoProject/logs/gunicorn-access.log

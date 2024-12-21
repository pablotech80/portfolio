# Etapa 1: Construcción
FROM python:3.11-slim AS builder

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

# Recolectar archivos estáticos
RUN python manage.py collectstatic --noinput

# Etapa 2: Imagen final
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias instaladas y archivos del proyecto
COPY --from=builder /app /app

# Exponer el puerto
EXPOSE 8000

# Comando para iniciar Gunicorn
CMD ["gunicorn", "DjangoProject.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]



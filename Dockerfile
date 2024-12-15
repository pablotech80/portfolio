# Imagen base de Python
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Crear el directorio de la aplicación
WORKDIR /app

# Copiar los requisitos
COPY requirements.txt /app/

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . /app/
COPY ./media /app/media

# Recolectar archivos estáticos
RUN python manage.py collectstatic --noinput

# Ejecutar migraciones
RUN python manage.py migrate

# Comando por defecto: Gunicorn
CMD ["gunicorn", "DjangoProject.wsgi:application", "--bind", "0.0.0.0:8000"]

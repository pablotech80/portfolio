# Usamos una versión consistente con lo que indica el proyecto
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

COPY requirements.txt .

# Instalamos las dependencias necesarias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    musl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiamos los archivos del proyecto al contenedor
COPY . /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# Instalamos las dependencias de Python usando el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 8000 para el servidor de Django
EXPOSE 8000

RUN python manage.py migrate

# Comando para ejecutar la aplicación usando Gunicorn
CMD ["gunicorn", "DjangoProject.wsgi:application", "--bind", "0.0.0.0:8000"]

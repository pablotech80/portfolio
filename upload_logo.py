import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader

# Cargar variables del .env
load_dotenv()

# Configurar Cloudinary usando la URL completa
cloudinary.config(
    cloud_name='dyanbg7xs',
    api_key=os.getenv("CLOUDINARY_URL").split(':')[1].replace('//', ''),
    api_secret=os.getenv("CLOUDINARY_URL").split(':')[2].split('@')[0]
)

# Subida del logo
upload_result = cloudinary.uploader.upload(
    "assets/bioanalyze_logo.JPG",
    public_id="bioanalyze_logo",
    overwrite=True,
    resource_type="image"
)

# Mostrar URL resultante
print("Imagen subida correctamente.")
print("URL sin transformación:", upload_result['secure_url'])
print("URL con transformación:")
print("https://res.cloudinary.com/dyanbg7xs/image/upload/ar_1:1,c_auto,g_auto,w_500,r_max/bioanalyze_logo")

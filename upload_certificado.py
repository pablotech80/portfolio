import os
from dotenv import load_dotenv

import cloudinary
import cloudinary.uploader

load_dotenv()

cloudinary.config(
    cloud_name='dyanbg7xs',
    api_key=os.getenv("CLOUDINARY_URL").split(':')[1].replace('//', ''),
    api_secret=os.getenv("CLOUDINARY_URL").split(':')[2].split('@')[0]
)

# Subida del certificado PDF
upload_result = cloudinary.uploader.upload(
    "assets/diploma1.jpg",
    public_id="diploma1",
    resource_type="auto",  # permite subir PDF
    overwrite=True
)

print("Subido correctamente")
print("URL directa:", upload_result["secure_url"])

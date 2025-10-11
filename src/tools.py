from PIL import Image
from nudenet import NudeDetector
from telethon.sync import TelegramClient
from telethon import functions, types

from typing import List

import math
import io

def nude_classifier(image_path: str) -> bool :
  detector = NudeDetector()
  
  NUDE_CLASSES = [
      'EXPOSED_BREAST_F',      # Senos expuestos
      'EXPOSED_GENITALIA_F',   # Genitales femeninos
      'EXPOSED_GENITALIA_M',   # Genitales masculinos  
      'EXPOSED_BUTTOCKS',      # Glúteos expuestos
      'EXPOSED_ANUS'           # Ano expuesto
  ]

  # Verificar si HAY DESNUDO
  detections = detector.detect(image_path)
  has_nudity = any(
      d['class'] in NUDE_CLASSES and d['score'] > 0.6 
      for d in detections
  )
  if has_nudity:
    return True
  else:
    return False

def image_optimize(image_path: str):
  try:
      # Open the image using Pillow
    with Image.open(image_path) as img:
      # Save the image to a temporary in-memory buffer
      buffer = io.BytesIO()
      img.save(buffer, format=img.format)  # Use the same format as the original image
      buffer_size = buffer.tell()  # Get the size in bytes
      
      # Convert bytes to megabytes (1 MB = 1024 * 1024 bytes)
      size_in_mb = buffer_size / (1024 * 1024)
      if size_in_mb >= 8 :
        print("imagen demasiado grande, redimensionando..")
        width, height = img.size
        img.resize(( math.ceil(width * 0.5), math.ceil(height*0.5)), Image.Resampling.BOX ).save(image_path)
        print(f"imagen redimensionanda a: {width}px x {height}px")
  except Exception as e:
      print(f"Error: {e}")
      return None
async def image_analizer( image_list: List[str]) :

  for img in image_list:
    image_optimize(img)
    # print("debnug 1")
    # isNude = nude_classifier(img)
    # print(f"is nude {isNude}")
    # # input_media = InputMediaUploadedPhoto(
    # #   file = await client.upload_file(img),
    # #   spoiler=isNude  # ← Spoiler solo para esta imagen
    # # )
    # # print("debnug 2")
    # # single_media = InputSingleMedia(
    # #     media=input_media,
    # #     message="⚠️ Contenido sensible" if isNude else "",
    # #     entities=[]
    # # )
    # print(f"file {img}")
    # uploaded_photo = await client.upload_file(img)
    # print(f"Archivo subido. ID temporal: {uploaded_photo.id}") 
    # inputMedia = types.InputSingleMedia(
    #     media=types.InputMediaUploadedPhoto(
    #         file = uploaded_photo,
    #         # **********************************************
    #         spoiler=isNude,  # <--- AGREGAR EL ATRIBUTO SPOILER AQUÍ
    #         # **********************************************
    #     ),
    #     message="⚠️ Contenido sensible" if isNude else "",
    # )
    # print("debnug 3")
    # media_list.append(inputMedia)

from telethon import TelegramClient
from telethon.tl.types import DocumentAttributeFilename
from telethon import functions, types

import os
import time
import shutil
from tools import image_analizer
# --- Configuración ---
API_ID = 22560648 # ¡Reemplaza con tu API ID de my.telegram.org/apps!
API_HASH = 'fe3c942e984d7d02e5c4482c521161ba' # ¡Reemplaza con tu API Hash!
BOT_TOKEN = '7638856065:AAHOpl1u91v5vf2m_STZV4MRXy56eOqDEe4' # ¡Reemplaza con tu token de BotFather!
GROUP_USERNAME = 'modelcollector3d' # O ID numérico: -123456789
UPLOAD_FOLDER = '/files/pendent'
TARGET_FOLDER = '/files/uploaded'
LOG_FILE = '/files/upload_log.txt'

client = TelegramClient('bot3', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

def log_upload(message):
  with open(LOG_FILE, 'a') as f:
    print(f"{time.ctime()}: {message}")
    f.write(f"{time.ctime()}: {message} \n")

async def getFirstFolder () -> str :
  """walk in UPLOAD_FOLDER and return first directory found"""
  folder = os.listdir(UPLOAD_FOLDER)[0]
  return folder

async def getFiles (folder_name: str) -> dict :
  """
  walk in folder_name and set values:
    stl = zip file that contains 3d file. Value is full path
    images = list of images. Value is full path for any image
  """
  stl = ""
  images = []
  for file in os.listdir(os.path.join(UPLOAD_FOLDER, folder_name)):
    if file.startswith(folder_name):
      stl = file
    else:
      image_path = os.path.join(UPLOAD_FOLDER, folder_name, file)
      images.append(image_path)
  return { "stl": os.path.join(UPLOAD_FOLDER, folder_name, stl),  "images": images }

async def main():
  try:
    print("starting app")
    if len(os.listdir(UPLOAD_FOLDER)) == 0:
      print("folder is empty. Nothing to do")
    else:
      folder_name = await getFirstFolder()
      files = await getFiles(folder_name)
      async with client.action(GROUP_USERNAME, 'document') as action:
        # sending stl
        print(f"trying to upload file: {files['stl']}")
        await image_analizer(files['images'])
        album0 = []
        album1 = []
        uploaded_file0 = await client.upload_file(files['images'][0])
        spoiler_media0 = types.InputMediaUploadedPhoto(
            uploaded_file0,
            spoiler=True
        )
        album0.append(spoiler_media0)
        uploaded_file1 = await client.upload_file(files['images'][1])
        spoiler_media1 = types.InputMediaUploadedPhoto(
            uploaded_file1,
            spoiler=False
        )
        album1.append(spoiler_media1)
        await client.send_file(
            GROUP_USERNAME,
            album0
        )
        await client.send_file(
            GROUP_USERNAME,
            album1
        )
        # await client.send_file(
        #   GROUP_USERNAME, 
        #   files['stl'],
        #   caption = "https://t.me/modelcollector3d",
        #   progress_callback=action.progress
        # )
        # # sending images
 
        

        # await client.send_file(
        #   GROUP_USERNAME, 
        #   files['images'],
        #   caption = f"{folder_name}",
        #   progress_callback=action.progress
        # )
        # # sending images

        # log_upload(f"subido exitosamente {files['stl']}")
        # shutil.move(
        #   os.path.join(UPLOAD_FOLDER, folder_name ),
        #   os.path.join(TARGET_FOLDER, folder_name )
        # )
  except Exception as e:
    print(f"Error found: {e}")

try:
  with client:
    while True:
      client.loop.run_until_complete(main())
      time.sleep(3600)
except Exception as e:
  print(f"Error: {e}")



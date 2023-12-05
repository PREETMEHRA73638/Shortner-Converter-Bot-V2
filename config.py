# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "28280795"))
API_HASH = os.environ.get("API_HASH", "3f02c2df6069de8c1a2abf623da0a4b8")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6351826749:AAGTaE62hlrZg369C6Ax7Cyo1J6WNd-R89w")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://G:g@cluster0.cbchwas.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6651109872")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6651109872)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001707609134")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MOVIES_VILLA_UPDATE") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/7de1d9ff50461400a22b6.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
SHORTNER_LINK = "lincopro.in"
CHANNEL_LINK = "https://t.me/Movies_villae"

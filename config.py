
import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG', default=None)

TOKEN = os.getenv('TELEGRAM_TOKEN')
OWM_TOKEN = os.getenv('OWM_TOKEN')

# webhook settings
WEBHOOK_HOST = os.getenv('HEROKU_APP_URL')
print(WEBHOOK_HOST, "@@@@@@@@@@@@@@@@@@@@@@@@@@12")
WEBHOOK_PATH = '/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = os.getenv('PORT', default=8000)
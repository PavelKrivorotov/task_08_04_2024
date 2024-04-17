import os
from pathlib import Path

import dotenv


PathDir = Path(__file__).parent
PathEnv = Path(PathDir.parent.parent, '.env')

dotenv.load_dotenv(dotenv_path=PathEnv)

# ...
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))

# Database
DATABASE = {
    'MIDDLWARE': os.getenv('DATABASE_MIDDLWARE'),
    'USER': os.getenv('DATABASE_USER'),
    'PASSWORD': os.getenv('DATABASE_PASSWORD'),
    'NAME': os.getenv('DATABASE_NAME'),
    'HOST': os.getenv('DATABASE_HOST'),
    'PORT': int(os.getenv('DATABASE_PORT'))
}

# Pgaination
PAGINATION = {
    'DEFAULT_COUNT_PER_PAGE': 50
}

# CORS
ALLOWED_HOSTS = ['*']

ALLOWED_ORIGINS = ['*']
ALLOW_CREDENTIALS = True
ALLOW_METHODS = ['*']
ALLOW_HEADERS = ['*']


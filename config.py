import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)


# ENV
ENV = os.getenv('ENV')

# Application
VERSION = os.getenv('VERSION')
LIMIT = os.getenv('LIMIT')

# Database (PostgreSQL)
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# JWT
JWT_PRIVATE_KEY = os.getenv('JWT_PRIVATE_KEY')
JWT_PUBLIC_KEY = os.getenv('JWT_PUBLIC_KEY')
JWT_EXPIRY = os.getenv('JWT_EXPIRY')
JWT_ISSUER = os.getenv('JWT_ISSUER')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')

# Log
LOG_FILE_NAME_FORMAT = os.getenv('LOG_FILE_NAME_FORMAT')
LOG_PATH = os.getenv('LOG_PATH')
LOG_LEVEL = os.getenv('LOG_LEVEL')
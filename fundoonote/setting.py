from dotenv import load_dotenv
import os
import logging

load_dotenv()


# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# project server setting
FUNDOO = {
    'host': os.getenv('HOST'),
    'port': int(os.getenv('PORT')),
    'base_url': os.getenv('BASE_URL')
}
# generate password using salt
password_salt = os.getenv('PASSWORD_SALT')

# database mysql
DATABASE = {
    'database': os.getenv('DATABASE'),
    'sqlite_db': os.getenv('SQLITE')
}
MYSQL_DB_CONFIG = {
    "user": os.getenv('DB_USERNAME'),
    "password": os.getenv('DB_PASSWORD'),
    "host": os.getenv('DB_HOST'),
    "db_name": os.getenv('DB_NAME'),
    "port": int(os.getenv("DB_PORT"))
}

# cache (redis)
CACHE = {
    'host': os.getenv('HOST'),
    'port': os.getenv('REDIS_PORT'),
    'decode_responses': os.getenv('CACHE_RESPONSE'),
    'password': os.getenv('REDIS_PASSWORD'),
    'db': 0
}

# email backend
EMAIL = {
    'email_host': os.getenv('EMAIL_HOST'),  # email host
    'email_port': os.getenv('EMAIL_PORT'),  # email port
    'email_host_username': os.getenv('EMAIL_HOST_USERNAME'),  # email host username
    'email_host_password': os.getenv('EMAIL_HOST_PASSWORD'),
}

# jwt auth configuration
AUTH = {
    'secret_key': os.getenv('JWT_SECRET'),
    'algorithms': os.getenv('JWT_ALGORITHMS')
}

AWS_S3 = {
    'region': os.getenv('AWS_REGION')
}
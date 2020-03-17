from dotenv import load_dotenv
import os
import logging

load_dotenv()


class ConfigService:
    # logger
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    # project server setting
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    base_url = os.getenv('BASE_URL')

    # database mysql
    DATABASE = {
        'database': os.getenv('DATABASE')
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
        'email_host': os.getenv('EMAIL_HOST'),
        'email_port': os.getenv('EMAIL_PORT'),
        'email_host_username': os.getenv('EMAIL_HOST_USERNAME'),
        'email_host_password': os.getenv('EMAIL_HOST_PASSWORD'),
    }

    # jwt auth configuration
    AUTH = {
        'secret_key': os.getenv('JWT_SECRET'),
        'algorithms': os.getenv('JWT_ALGORITHMS')
    }


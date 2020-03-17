from datetime import datetime, timedelta
import jwt
from setting import ConfigService

obj = ConfigService


class JwtToken:

    @staticmethod
    def create_jwt_token(id):
        payload = {'id': id, 'exp': datetime.utcnow() + timedelta(seconds=10000)}
        encoded_token = jwt.encode(payload, obj.AUTH['secret_key'], obj.AUTH['algorithms']).decode('utf-8')
        return encoded_token

    @staticmethod
    def decode_jwt_token(token):
        decoded_token = jwt.decode(token, obj.AUTH['secret_key'], obj.AUTH['algorithms'])
        return decoded_token

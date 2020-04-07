from datetime import datetime, timedelta
import jwt
from setting import AUTH

class JwtToken:

    @staticmethod
    def create_jwt_token(id):  # create jwt token
        try:
            if id is not None:
                payload = {'id': id,
                           'exp': datetime.utcnow() + timedelta(seconds=10000)}  # payload 'exp' is time set of
                # token
                encoded_token = jwt.encode(payload, AUTH['secret_key'], AUTH['algorithms']).decode('utf-8')
                return encoded_token  # return encoded
            else:
                return ValueError("else it returns token is None")
        except:
            raise Exception("Please enter valid payload or keys")

    @staticmethod
    def decode_jwt_token(token):
        try:
            if token is not None:  # if token is not None the decode  it
                decoded_token = jwt.decode(token, AUTH['secret_key'], AUTH['algorithms'])
                return decoded_token
            else:
                return ValueError("else it returns token is None")
        except:
            raise Exception("Please enter valid payload or keys")

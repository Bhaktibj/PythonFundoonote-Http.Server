from fundooNotes.common.response import Response
from fundooNotes.config.cache_connection import RedisService
from fundooNotes.auth.jwt_token import JwtToken
import jwt

jwt_obj = JwtToken
redis_obj = RedisService()

response = {
    'message': "something went wrong"
}


def app_login_required(method):

    def token_varification(self):
        try:
            print(self.path, type(self.path))
            if self.path in ['/note/api/create', '/note/api/list', '/note/api/update','/change_password', '/note/api/delete']:
                token = self.headers['token']
                payload_data = jwt_obj.decode_jwt_token(token)
                user_id_key = payload_data['id']
                token = redis_obj.get_value(user_id_key)
                if token is None:
                    raise ValueError("You Need To Login First")
                return method(self)
            else:
                return method(self)
        except jwt.ExpiredSignatureError:
            response['message'] = "token signature expired"
            Response(self).jsonResponse(status=404, data=response)
        except jwt.DecodeError:
            response['message'] = "decode error"
            Response(self).jsonResponse(status=404, data=response)
    return token_varification

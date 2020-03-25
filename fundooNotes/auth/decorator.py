from ..common.response import Response
from ..urls.api_urls import urls
from ..common.utils import cache, jwt_obj
import jwt

response = {
    'message': "something went wrong"
}


def app_login_required(method):
    def token_varification(self):
        try:
            if self.path not in [urls['register'], urls['login']]:  # check self.path is in urls list or not if yes then it returns True
                token = self.headers['token']  # take headers token
                print(token)
                payload_data = jwt_obj.decode_jwt_token(token)   # decode the token
                print(payload_data)
                user_id_key = payload_data['id']   # get user_id from token
                print(user_id_key)
                token = cache.get_value(user_id_key)  # re-validate in redis to pass key if token is found-True
                if token is None:
                    raise ValueError("You Need To Login First")
                return method(self)
            else:
                return method(self)
        except jwt.ExpiredSignatureError:
            response['message'] = "token signature expired"  # if token is expired from cache
            Response(self).jsonResponse(status=404, data=response)
        except jwt.DecodeError:
            response['message'] = "decode error" # if token is not valid or None
            Response(self).jsonResponse(status=404, data=response)
    return token_varification

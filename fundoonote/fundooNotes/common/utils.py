from fundooNotes.config.cache_connection import CacheService
from fundooNotes.common.serializer import AlchemyEncoder
from easy_profile import SessionProfiler
from fundooNotes.auth.jwt_token import JwtToken
from setting import password_salt
import json
import re
import bcrypt

serializer = AlchemyEncoder  # create Serializer class object
cache = CacheService()  # create cache service object
profiler = SessionProfiler()
jwt_obj = JwtToken  # create jwt object


def json_response(success=False, message='bad request', data=None):
    """ this  method used for return the json response is dictionary format """
    response = {'success': success,
                "message": message,
                "data": data}
    return response


def serialize_data(object):
    """ this method is used for convert object data into json format"""
    serializer_data = json.dumps(object, cls=AlchemyEncoder)
    data = json.loads(serializer_data)  # and loads the data
    return data  # return the data


def email_validation(email):
    """ this method is used for validate the email"""
    if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):  # email validation like "bhakti@gmail.com"
        return True
    else:
        return False


def password_validation(password):
    """ This method is used for validate the email format"""
    if bool(re.search(r'[A-Za-z0-9@#$%^&+=]{8,}', password)):  # password validation like Bhakti@123
        return True
    else:
        return False


def hash_password(password):
    """ This method is used generate the hash password"""
    password = password.encode()  # convert str to bytes
    salt = password_salt.encode()  # convert salt string to bytes
    hashed_password = bcrypt.hashpw((password), salt) # generate hash password
    if hashed_password is not None:  # check pass word is none or not
        return hashed_password  # if not none
    else:
        return None # else None

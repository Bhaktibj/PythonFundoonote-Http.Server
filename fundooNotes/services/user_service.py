from easy_profile import SessionProfiler
from ..auth.jwt_token import JwtToken as jwt_obj
from ..config.cache_connection import RedisService
from ..models.model import Users
from ..mail.send_email import SendMail
from ..common.response import JsonResponse as obj
from ..config.database_connection import DatabaseService
from logzero import logger
from ..config.s3_connections import BotoService
boto = BotoService

profiler = SessionProfiler()
db_obj = DatabaseService()
mail_obj = SendMail()
cache_obj = RedisService()

class UserServices:

    def __init__(self):
        pass

    def register(self, data):
        logger.info("register test case")
        with profiler:
            user = db_obj.filter_by(tabel=Users,email=data['email'])
            if user:
                return obj.response(success=False, message="User is already exist", data=profiler.stats)
            else:
                users = Users(username=data['username'], password=data['password'], email=data['email'])
                if users:
                    db_obj.save_into_db(users)
                    return obj.response(success=True, message="Successfully registered user", data=data)
                else:
                    return obj.response(success=False, message="Please enter proper format", data=[])

    def login(self, data):
        with profiler:
            user = db_obj.session.query(Users).filter_by(email=data['email'], password=data['password']).first()
            if user:
                token = jwt_obj.create_jwt_token(id=user.id)
                print(token)
                cache_obj.set_key(key=user.id, value=token)
                cache_obj.set_key(key="login_id", value=user.email)
                return obj.response(success=True, message="Successfully login user", data=token)
            else:
                return obj.response(success=False, message="Check user credentials", data=data)

    def forgot(self, data, version, host):
        with profiler:
            user = db_obj.filter_by(tabel=Users, email=data['email'])
            if user:
                email = data['email']
                print(data)
                encoded_token = jwt_obj.create_jwt_token(email)
                data = f"{host}://{version}/reset/?token={encoded_token}"
                print(data)
                mail_obj.send_mail(email, data)
                return obj.response(success=True, message="Message successfully sent", data=profiler.stats)
            else:
                return obj.response(success=False, message="user does not exist", data=data)

    def reset_password(self, data, email):
        if email and data is not None:
            with profiler:
                db_obj.update_query(tabel=Users, email=email, password=data['password'])
                return obj.response(success=True, message="Password Reset successfully", data=profiler.stats)
        else:
            return obj.response(success=False, message="something went wrong", data=[])

    def change_password(self, data):
        login_user = cache_obj.get_value('login_id')
        try:
            user = db_obj.filter_by(tabel=Users, email=login_user)
            if user and user.password == data['current_password']:
                if user.password != data['new_password']:
                    db_obj.update_query(tabel=Users, email=user.email, password=data['new_password'])
            else:
                return obj.response(message="user does not exist or password mismatch")
        except:
            return obj.response(message="password is too same please enter another password")
        return obj.response(success=True, message="Successfully reset password", data=data)

    def logout_user(self):
        login_user = cache_obj.get_value('login_id')
        if login_user is not None:
            cache_obj.delete('login_id')
            return obj.response(success=True, message="logout user successfully")
        else:
            return obj.response("already logout user")

    def s3_upload(self, data):
        region = 'ap-south-1'
        if data['image'] is None:
            return {'image is none'}
        result = boto.bucket_exist(self, bucket_name=data['bucket_name'])
        if result is False:
            boto.create_bucket(self, bucket_name=data['bucket_name'], region=region)
            boto.upload_files(self, upload_file=data['image'], bucket_name=data['bucket_name'],
                              file_name=data['file_name'])
            return obj.response(success=True,
                                message="Successfully created new bucket" + data['bucket_name'] + "and uploaded image",
                                data=data)
        else:
            boto.upload_files(self, upload_file=data['image'], bucket_name=data['bucket_name'],
                              file_name=data['file_name'])
            return obj.response(success=True, message="Successfully uploaded image", data=data)

    def get_s3_objects(self, data):
        result = boto.bucket_exist(self, bucket_name=data['bucket_name'])
        images = []
        if result is True:
            objects = boto.list_bucket_objects(self, data['bucket_name'])  # listing object from bucket function
            if objects is not None:  # if objects is not none
                list = []
                for object in objects:
                    list.append(object)
                for i in list:
                    bucket_object = f' {i["Key"]}'
                    print("Image_name", bucket_object)
                    images.append(bucket_object)
                print(list)
                return obj.response(success=True, message="successfully listing objects from bucket", data=images)
            else:
                return obj.response(success=False, message="empty bucket", data=[])
        else:
            return obj.response(success=False, message="does not exist bucket", data=[])
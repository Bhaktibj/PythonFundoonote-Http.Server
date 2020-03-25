from ..models.model import Users
from ..common.db_operation import *
from ..common.utils import email_validation, password_validation, cache, profiler, jwt_obj, json_response, hash_password
from ..common.send_email import SendMail


# from ..config.s3_connections import BotoService, region
# boto = BotoService


class UserServices:
    """ This class is used for creating the service api"""
    def __init__(self):
        pass

    def register(self, data):
        """ This method is used for register the user"""
        try:
            if email_validation(email=data['email']):
                # check email is valid format or not if valid
                user = filter_by(table=Users, email=data['email'])  # check user is  exist or not
                if user:
                    return json_response(message="User is already exist")
                else:
                    if password_validation(password=data['password']):
                        hashed_password = hash_password(password=data['password'])
                        users = Users(first_name=data['first_name'],last_name=data['last_name'],password=hashed_password,
                                      email=data['email'])  # create user
                        save(users)  # save the user
                        return json_response(success=True, message="Successfully registered user",
                                             data=data)
                    else:
                        return json_response("enter valid password in valid format")
            else:
                return json_response(message="please enter valid email-id in valid format")
        except:
            return json_response(message="missing values or wrong format")


    def login(self, data):
        """ This method is used for login the user"""
        try:
            with profiler:
                if email_validation(email=data['email']):
                    hashed_password = hash_password(data['password'])
                    if hashed_password is not None:
                        user = session.query(Users).filter_by(email=data['email'], password=hashed_password).first()
                        if user is not None:  # check the user is none or not if note
                            token = jwt_obj.create_jwt_token(id=user.id)  # create the jwt token
                            cache.set_key(key=user.id, value=token)  # set the jwt token is cache with user.id
                            cache.set_key(key="login_id", value=user.id)  # set login user id in cache with "login_id" key
                        else:
                            return json_response(success=False, message="Check user credentials", data=data)  # return false
                    else:
                        return json_response("password is not hashed")
                else:
                    return json_response(message="please enter valid email-id in valid format")
        except:
            return json_response("missing values or invalid data")
        return json_response(success=True, message="Successfully login user", data=token)  # return success

    def forgot(self, data, version, host):
        """ This method is used for forgot password"""
        try:
            with profiler:
                if email_validation(email=data['email']):
                    user = filter_by(table=Users, email=data['email'])  # filter the email from Users table
                    if user is not None:
                        email = data['email']
                        encoded_token = jwt_obj.create_jwt_token(email)  # create the jwt token
                        data = f"{host}://{version}/reset/?token={encoded_token}"  # create reset token
                        send_mail_service = SendMail()  # create send_mail object
                        send_mail_service.send_mail(email=email, data=data)  # send the email for forgot password
                    else:
                        return json_response(success=False, message="user does not exist", data=data)  # does not exist
                else:
                    return json_response("enter valid email in valid format")
        except:
            return json_response("missing values or invalid data")
        return json_response(success=True, message="Message successfully sent",
                             data=data)  # return the response

    def reset_password(self, data, email):
        """ this method is used to reset password"""
        try:
            if email is not None:  # if email and data is not none
                with profiler:
                    if password_validation(password=data['password']):
                        hashed_password = hash_password(password=data['password'])
                        if hashed_password is not None:
                            update(table=Users, email=email, password=hashed_password
                                   )  # update the password
                            return json_response(success=True, message="Password Reset successfully", data=profiler.stats)
                        else:
                            return json_response("password is not hashed")
                    else:
                        return json_response("please enter valid password in valid format")
        except:
            return json_response("email is none or something went wrong")  # return false response

    def change_password(self, data):
        """ This method is used for change the password"""
        try:
            login_user = cache.get_value('login_id')  # take the login_user from cache using "login_id" key
            user = filter_by_id(table=Users, id=login_user)  # filter this id is exist in database or not
            if user and user.password == hash_password(password=data['current_password']):  # check current pass and user.pass is same or not, if same
                if user.password != data['new_password']:  # check user.password and new password is same or not, if not
                    update(table=Users, email=user.email, password=hash_password(password=data['new_password']))  # update password
                else:
                    return json_response(
                        "password is too same please enter another password")  # return password is too same
            else:
                return json_response("user does not exist or password mismatch")  # return does not exist
        except:
            return json_response("missing values or invalid data")  # return password is too same
        return json_response(success=True, message="Successfully reset password",
                             data=data)  # return the success response

    def logout_user(self):
        """ this method is used for logout user"""
        login_user = cache.get_value('login_id')  # get login_user id from cache
        print(login_user)
        if login_user is not None:  # is login user is not None
            cache.delete('login_id')  # delete the login user id  from cache
            return json_response(success=True, message="logout user successfully")  # return success response
        else:
            return json_response("already logout user")  # return false response

    # def s3_upload(self, data):
    #     """ This method is used for upload the image on s3 bucket"""
    #     try:
    #         if data['image'] is None: # check image is  None or not
    #             return json_response(" Image is None") # if image is None
    #         result = boto.bucket_exist(bucket_name=data['bucket_name'])  # check bucket is exist or not
    #         if result is False:  # if result is false
    #             boto.create_bucket(bucket_name=data['bucket_name'], region=region) # create the new bucket  and uplaod image
    #             boto.upload_files(upload_file=data['image'], bucket_name=data['bucket_name'],  # upload image
    #                               file_name=data['file_name'])
    #             return json_response(success=True,
    #                                  message="Successfully created new bucket" + data['bucket_name'] + "and uploaded image",
    #                                  data=data) # return new bucket and uploaded image
    #         else:
    #             boto.upload_files(upload_file=data['image'], bucket_name=data['bucket_name'],
    #                               file_name=data['file_name'])  # if bucket is exist uploaded the image
    #             return json_response(success=True, message="Successfully uploaded image", data=data) # return success response
    #     except:
    #         return json_response("missing values or invalid data")
    #
    # def get_s3_objects(self, data):
    #     """ This method is used to get object from s3 bucket"""
    #     try:
    #         result = boto.bucket_exist(bucket_name=data['bucket_name'])  # check bucket is exist or not
    #         images = []
    #         if result is True: # if result is true
    #             objects = boto.list_bucket_objects(data['bucket_name'])  # listing object from bucket function
    #             if objects is not None:  # if objects is not none
    #                 list = []
    #                 for object in objects: # return object from objects
    #                     list.append(object) # append in list
    #                 for image in list: # take images from list
    #                     bucket_object = f' {image["Key"]}' # return image name
    #                     print("Image_name", bucket_object)
    #                     images.append(bucket_object) # append the image objects in images list
    #                 print(list)
    #                 # return all images response
    #                 return json_response(success=True, message="successfully listing objects from bucket", data=images)
    #             else:
    #                 return json_response(success=False, message="empty bucket", data=[]) # return empty bucket
    #         else:
    #             return json_response(success=False, message="does not exist bucket", data=[]) # does not exist bcuket
    #     except:
    #         return json_response("password is too same please enter another password")  # return password is too same
    #

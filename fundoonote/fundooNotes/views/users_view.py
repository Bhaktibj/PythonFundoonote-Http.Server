import cgi
import cgitb
cgitb.enable()
from ..services.user_service import UserServices
from ..common.utils import json_response
user_service = UserServices()


class UserDetails:
    """ This class is used for create the all user views """
    def __init__(self):
        pass

    def for_registration(self):
        """ This view is used  for registration """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:   # enter the try block
            data = {'first_name': form['first_name'].value, 'last_name': form['last_name'].value,
                    'password': form['password'].value, 'email': form['email'].value}
            response_data = user_service.register(data)  # send data to service and return response
            return response_data  # return response
        except KeyError:  # enter except block
            return json_response("missing values or invalid data")

    def for_login(self):
        """ This view is used for login user """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'email': form['email'].value, 'password': form['password'].value}
            response_data = user_service.login(data)
            return response_data
        except KeyError:
            return json_response("missing values or invalid data")

    def forgot_password(self, version):
        """ this view method is used for forgot the password"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            version = version.split('/')[0]
            host = self.headers['Host']
            data = {'email': form['email'].value}
            print(data)
            response_data = user_service.forgot(data, host, version)
            return response_data
        except KeyError:
            return json_response("missing values or invalid data")

    def set_password(self, email_id):
        """ this method is used for set password"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'password': form['password'].value}
            print(data)
            response_data = user_service.reset_password(data, email=email_id)
            return response_data
        except KeyError:
            return json_response("missing values or invalid data")

    def change_password(self):
        """ this method is used for change password"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'current_password': form['current_password'].value, 'new_password': form['new_password'].value}
            response_data = user_service.change_password(data)
            return response_data
        except KeyError:
            return json_response("missing values or invalid data")

    def logout_user(self):
        response_data = user_service.logout_user()
        return response_data

    def upload_profile(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'image': form['image'].value, 'bucket_name': form['bucket_name'].value, 'file_name': form['file_name'].value}
            response_data = user_service.s3_upload(data)
            return response_data
        except KeyError:
            return json_response("missing values or wrong format")

    def get_object_from_bucket(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'bucket_name': form['bucket_name'].value}
            response_data = user_service.get_s3_objects(data)
            return response_data
        except KeyError:
            return json_response("missing values or wrong format")

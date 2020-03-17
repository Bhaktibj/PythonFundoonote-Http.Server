import cgi
from ..services.user_service import UserServices
from fundooNotes.common.response import Response

import cgitb

cgitb.enable()
user = UserServices()


class UserDetails:
    def __init__(self):
        pass

    def for_registration(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'username': form['username'].value, 'password': form['password'].value, 'email': form['email'].value}
        print(data)
        response_data = user.register(data)
        print("rese", response_data)
        return response_data

    def for_login(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'email': form['email'].value, 'password': form['password'].value}
        response_data = user.login(data)
        return response_data

    def forgot_password(self, version):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        version = version.split('/')[0]
        host = self.headers['Host']
        data = {'email': form['email'].value}
        print(data)
        response_data = user.forgot(data, host, version)
        return response_data

    def set_password(self, email_id):
        print(self.headers)

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        data = {'password': form['password'].value}
        print(data)
        response_data = user.reset_password(data, email=email_id)
        print(response_data)
        return response_data

    def change_password(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'current_password': form['current_password'].value, 'new_password': form['new_password'].value}
        print(data)
        response_data = user.change_password(data)
        return response_data

    def logout_user(self):
        response_data = user.logout_user()
        return response_data

    def upload_profile(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'image': form['image'].value, 'bucket_name': form['bucket_name'].value, 'file_name': form['file_name'].value}
        response_data = user.s3_upload(data)
        return response_data

    def get_object_from_bucket(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'bucket_name': form['bucket_name'].value}
        response_data = user.get_s3_objects(data)
        return response_data
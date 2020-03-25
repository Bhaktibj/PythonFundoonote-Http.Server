from http.server import BaseHTTPRequestHandler
from fundooNotes.common.response import Response
from fundooNotes.views.notes_view import NoteDetails
from fundooNotes.views.users_view import UserDetails
from fundooNotes.auth.jwt_token import JwtToken as jwt_obj
from fundooNotes.urls.api_urls import urls
from fundooNotes.auth.decorator import app_login_required


class RequestHandler(BaseHTTPRequestHandler):
    """ This class is used for handle all request method Head, do_post, do_get that arrives at server"""

    def _set_headers(self):  # set headers
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

    # def _read_data(self):
    #     length = int(self.headers['Content-Length'])
    #     content = self.rfile.read(length)
    #     temp = json.loads(content.decode('utf-8'))
    #     return temp

    @app_login_required
    def do_POST(self):
        """ request the do_POST method"""
        user_details = UserDetails  # create class obj to call user views
        note_details = NoteDetails  # create class object for note views
        version = self.protocol_version  # declare protocol version
        try:
            if self.path.endswith(urls['register']):  # if self.path is  endswith urls[key]
                response_data = user_details.for_registration(self)
                Response(self).jsonResponse(status=200, data=response_data)  # return the view response

            elif self.path.endswith(urls['login']):  # if self.path is  endswith urls[key]
                response_data = user_details.for_login(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['forgot']):  # if self.path is  endswith urls[key]
                self._set_headers()
                response_data = user_details.forgot_password(self, version=version)
                Response(self).jsonResponse(status=200, data=response_data)

            elif 'token' in self.path:  # check 'token' is in self.path or not  if yes
                self._set_headers()
                from urllib.parse import urlparse, parse_qs  # using urllib.parse
                query_comp = parse_qs(urlparse(self.path).query)  # parse the request
                token = query_comp["token"][0]  # token is index of 0
                token_data = jwt_obj.decode_jwt_token(token)  # decode the token
                response_data = user_details.set_password(self,
                                                          token_data['id'])  # and get decode_id & for set_password
                Response(self).jsonResponse(status=200, data=response_data)  # if set_password is True return response

            elif self.path.endswith(urls['change_password']):  # if self.path is endswith urls[key]
                self._set_headers()  # set headers
                response_data = user_details.change_password(self)  # call the view and return the response
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['create_note']):  # if self.path is  endswith urls[key]
                self._set_headers()  # set headers
                response_data = note_details.create_note(self)  # call the view and return the response
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['read_note']):  # if self.path is endswith urls[key]
                self._set_headers()  # set headers
                response_data = note_details.read_note(self)  # call the view and return the response
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['update_note']):  # if self.path is endswith urls[key]
                self._set_headers()  # set headers
                response_data = note_details.update_note(self)  # call update view and return response
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['pin_note']):  # # if self.path is endswith urls[key]
                self._set_headers()  # set headers
                response_data = note_details.pin_note(self)  # call pin note view and return response
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['archive_note']):
                self._set_headers()
                response_data = note_details.archive_note(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['trash_note']):
                self._set_headers()
                response_data = note_details.trash_note(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['restore_note']):
                self._set_headers()
                response_data = note_details.archive_note(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['collaborate_note']):
                self._set_headers()
                response_data = note_details.collaborator_note(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['list_user_note']):
                self._set_headers()
                response_data = note_details.list_for_user_notes(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['upload_image_s3']):
                self._set_headers()
                response_data = user_details.upload_profile(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith(urls['get_image_s3']):
                self._set_headers()
                response_data = user_details.get_object_from_bucket(self)
                Response(self).jsonResponse(status=200, data=response_data)

        except IOError as e:  # if self.path is not found
            self.send_error(404, 'File Not Found %s', self.path)  # send error file not found

    def do_GET(self):
        """ request do_GET method"""
        user_details = UserDetails  # create UserDetail object
        note_details = NoteDetails

        if self.path.endswith(urls['logout']):
            self._set_headers()
            response_data = user_details.logout_user(self)
            Response(self).jsonResponse(status=200, data=response_data)

        elif self.path.endswith(urls['list_note']):
            self._set_headers()
            response_data = note_details.list_notes(self)
            Response(self).jsonResponse(status=200, data=response_data)

        elif self.path.endswith(urls['list_archive_note']):
            self._set_headers()
            response_data = note_details.list_for_archive_notes(self)
            Response(self).jsonResponse(status=200, data=response_data)

        elif self.path.endswith(urls['list_restore_note']):
            self._set_headers()
            response_data = note_details.list_for_restore_notes(self)
            Response(self).jsonResponse(status=200, data=response_data)

        elif self.path.endswith(urls['list_pin_note']):
            self._set_headers()
            response_data = note_details.list_for_pin_notes(self)
            Response(self).jsonResponse(status=200, data=response_data)

        elif self.path.endswith(urls['list_coll_note']):
            self._set_headers()
            response_data = note_details.read_collaborator_notes_list(self)
            Response(self).jsonResponse(status=200, data=response_data)

    def do_DELETE(self):
        """ request the do_Delete method"""
        note_details = NoteDetails
        if self.path.endswith(urls['delete_note']):
            self._set_headers()
            response_data = note_details.delete_note(self)
            Response(self).jsonResponse(status=200, data=response_data)

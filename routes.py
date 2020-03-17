from http.server import BaseHTTPRequestHandler
from fundooNotes.common.response import Response
from fundooNotes.views.notes_view import NoteDetails
from fundooNotes.views.users_view import UserDetails
from fundooNotes.auth.jwt_token import JwtToken as jwt_obj

class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

    # def _read_data(self):
    #     length = int(self.headers['Content-Length'])
    #     content = self.rfile.read(length)
    #     temp = json.loads(content.decode('utf-8'))
    #     return temp

    def do_POST(self):

        user_details = UserDetails
        note_details = NoteDetails
        version = self.protocol_version

        try:
            if self.path.endswith('/register'):  # signup user

                self._set_headers()
                response_data = user_details.for_registration(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith('/login'):
                self._set_headers()
                response_data = user_details.for_login(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith('/forgot'):
                self._set_headers()
                response_data = user_details.forgot_password(self, version=version)
                Response(self).jsonResponse(status=200, data=response_data)

            elif 'token' in self.path:
                self._set_headers()
                from urllib.parse import urlparse, parse_qs
                query_comp = parse_qs(urlparse(self.path).query)
                token = query_comp["token"][0]
                token_data = jwt_obj.decode_jwt_token(token)
                response_data = user_details.set_password(self, token_data['id'])
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith('/change_password'):
                self._set_headers()
                response_data = user_details.change_password(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith('/note/api/create'):
                self._set_headers()
                response_data = note_details.create_note(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith('/note/api/get'):
                self._set_headers()
                response_data = note_details.read_note(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith('/note/api/update'):
                self._set_headers()
                response_data = note_details.update_note(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith('/note/api/coll'):
                self._set_headers()
                response_data = note_details.collaborator_note(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith('/note/api/readnote'):
                self._set_headers()
                response_data = note_details.read_note_by_user(self)
                Response(self).jsonResponse(status=200, data=response_data)

            elif self.path.endswith('/upload'):
                self._set_headers()
                response_data = user_details.upload_profile(self)
                Response(self).jsonResponse(status=200, data=response_data)

        except IOError as e:
            self.send_error(404, 'File Not Found %s', self.path)

    # Logout
    def do_GET(self):

        note_details = NoteDetails
        user_details = UserDetails

        if self.path.endswith('/logout'):
            self._set_headers()
            response_data = user_details.logout(self)
            Response(self).jsonResponse(status=200, data=response_data)

        elif self.path.endswith('/note/api/list'):
            self._set_headers()
            response_data = note_details.get_notes(self)
            Response(self).jsonResponse(status=200, data=response_data)

        elif self.path.endswith('/note/api/archive'):
            self._set_headers()
            response_data = note_details.archive_note(self)
            Response(self).jsonResponse(status=200, data=response_data)

        elif self.path.endswith('/note/api/restore'):
            self._set_headers()
            response_data = note_details.restore_note(self)
            Response(self).jsonResponse(status=200, data=response_data)

        elif self.path.endswith('/note/api/pin'):
            self._set_headers()
            response_data = note_details.pin_notes(self)
            Response(self).jsonResponse(status=200, data=response_data)

    def do_DELETE(self):
        note_details = NoteDetails
        if self.path.endswith('/note/api/delete'):
            self._set_headers()
            response_data = note_details.delete_note(self)
            Response(self).jsonResponse(status=200, data=response_data)


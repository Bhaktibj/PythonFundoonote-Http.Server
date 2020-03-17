# from fundooNotes.urls.user_urls import Userurls
# from fundooNotes.common.response import Response
# from http.server import BaseHTTPRequestHandler
# from fundooNotes.views.users_view import UserDetails
#
# url_obj = Userurls
# user_details = UserDetails
#
#
# class RequestHandler(BaseHTTPRequestHandler):
#
#     def _set_headers(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/json")
#         self.end_headers()
#
#     def do_POST(self):
#         url_list = url_obj.url_fun(self)
#         print(url_list)
#         if self.path == url_list['/register']:
#             print("register")
#         elif self.path == url_list['/login']:
#             print("login")
#

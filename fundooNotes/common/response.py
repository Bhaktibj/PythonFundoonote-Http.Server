import json


class JsonResponse:
    @staticmethod
    def response(success=False, message='bad request', data=None):
        response = {'success': success,
                    "message": message,
                    "data": data, }
        return response


class Response:

    def __init__(self, response):
        self.Response = response

    def jsonResponse(self, status, data):
        self.Response.send_response(status)
        self.Response.send_header('Content-type', 'text/json')
        self.Response.end_headers()
        self.Response.wfile.write(json.dumps(data).encode())

import json


class Response:
    """ This class is used for return the response on server"""
    def __init__(self, response):
        self.Response = response  # initialize the class object

    def jsonResponse(self, status, data):
        """ This method is used for create the json-response"""
        self.Response.send_response(status)  # send the status code
        self.Response.send_header('Content-type', 'text/json') # send the headers
        self.Response.end_headers()
        self.Response.wfile.write(json.dumps(data).encode()) # encode the json data send on server

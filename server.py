from routes import RequestHandler
from http.server import HTTPServer
from setting import ConfigService

obj = ConfigService()

if __name__ == '__main__':
    server = HTTPServer((obj.host, obj.port), RequestHandler)
    print(f"httpd server start on {obj.host}:{obj.port}")
    server.serve_forever()
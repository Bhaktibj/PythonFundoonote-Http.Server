from routes import RequestHandler
from http.server import HTTPServer
from setting import FUNDOO


if __name__ == '__main__':
    server = HTTPServer((FUNDOO['host'], FUNDOO['port']), RequestHandler)
    print(f"httpd server start on {FUNDOO['host']}:{FUNDOO['port']}")
    server.serve_forever()
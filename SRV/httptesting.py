from threading import Thread
from time import sleep
from http import client
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        if post_data == b'Alice':
            self.send_response(200, "Thanks, for calling " + post_data.decode())
            self.end_headers()
            self.wfile.write(b"Got POST request from " + post_data)
        else:
            self.send_response(403)
            self.end_headers()

httpd = HTTPServer(('localhost', 8001), SimpleHTTPRequestHandler)
server = Thread(target=httpd.serve_forever)
server.start()
sleep(0.5)

h1 = client.HTTPConnection('localhost', 8001)
h1.request("GET", "/")
res = h1.getresponse()
print(res.status, res.reason)
data = res.read()
print(data)

h1.request("POST", "/", b"Bob")

res = h1.getresponse()
print(res.status, res.reason)
data = res.read()
print(data)

httpd.shutdown()

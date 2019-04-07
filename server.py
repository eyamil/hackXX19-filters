from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import os
from io import BytesIO

DEFAULT_PORT = 8080

def route(path):
    path = path.lstrip("/")
    if path == "":
        print("Trying to get public/index.html")
        return("public/index.html")
    else:
        print("Trying to get " + "public/" + path)
        return("public/" + path)

class Handler(BaseHTTPRequestHandler):

    def set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.set_headers()
        self.path = route(self.path)
        if os.path.isfile(self.path):
            f = open(self.path)
            self.wfile.write(bytes(f.read(), "utf-8"))
            f.close()
            return
        else:
            self.wfile.write("404 not found")
            return
        # Return file if it exists
        # Otherwise return "404 not found"

    def do_POST(self):
        self.set_headers()
        content_length = int()

def run_server(server_class = HTTPServer, handler_class = Handler, port = DEFAULT_PORT):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting server at port " + str(port))
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run_server(port = int(argv[1]))
    else:
        run_server()

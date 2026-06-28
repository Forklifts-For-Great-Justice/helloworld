from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Hello from {os.environ.get('PROJECT_NAME', 'app')}!\n".encode())

    def do_POST(self):
        if self.path == "/echo":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    port = int(os.environ.get("SERVER_PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Server starting on port {port}")
    server.serve_forever()

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

if __name__ == "__main__":
    port = int(os.environ.get("SERVER_PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Server starting on port {port}")
    server.serve_forever()

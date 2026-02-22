#!/usr/bin/python3
"""
Simple HTTP server using http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

print("File is running...")

class SimpleAPI(BaseHTTPRequestHandler):
    """
    Custom request handler for our simple API
    """

    def do_GET(self):
        """
        Handle GET requests
        """

        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # /data endpoint
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # /status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # /info endpoint (based on expected output example)
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Undefined endpoints
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    """
    Start the HTTP server
    """
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPI)
    print("Server running on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
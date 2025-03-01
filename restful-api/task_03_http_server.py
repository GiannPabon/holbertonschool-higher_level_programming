#!/usr/bin/env python3
"""
Task 3: Simple API using Python's http.server
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests:
          /       -> "Hello, this is a simple API!"
          /data   -> JSON response
          /status -> "OK"
          others  -> 404
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(sample_data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run_server(port=8000):
    print(f"Starting server on port {port}")
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()

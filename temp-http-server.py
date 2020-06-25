#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler,HTTPServer
import json
import subprocess

class Handler(BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header('Content-type', 'application/json')
        s.end_headers()
        value = subprocess.getoutput('vcgencmd measure_temp')
        response = {'cpu_temp': value.split('=')[1].split("'")[0]}
        s.wfile.write(json.dumps(response).encode())


httpd = HTTPServer(('', 8000), Handler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()

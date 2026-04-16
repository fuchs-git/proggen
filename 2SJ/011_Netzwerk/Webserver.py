from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Server läuft auf Port 8000...")
httpd.serve_forever()
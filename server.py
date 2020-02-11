import http.server
import socketserver

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("le server est demareé sur le PORT ", PORT)
    httpd.serve_forever()
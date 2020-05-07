import http.server
import socketserver
import threading

PORTS = [8080, 8081, 8082]
Handler = http.server.SimpleHTTPRequestHandler

def create_server(port):
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print("serving at port", port)
            httpd.serve_forever()
    except: # catch *all* exceptions
        print("Another service running at port", port)

for port in PORTS:
    threading.Thread(target=create_server, args=[port]).start()

import http.server
import socketserver
import threading

PORTS = [22, 25, 80, 443, 4000, 4001, 4002, 5000, 5500, 5432, 5433, 5577, 8888, 9988, 9011,  9999, 27017, 2080]
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


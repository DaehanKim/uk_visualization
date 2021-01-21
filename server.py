import http.server
import socketserver
import os

PORT = 8000

# os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("localhost", PORT), Handler)
print("serving at port", PORT)

try : 
	httpd.serve_forever()
except KeyboardInterrupt:
	print("User shutting down the server...")
	exit()
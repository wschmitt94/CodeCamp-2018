import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class myHandler(BaseHTTPRequestHandler):

	def do_GET():
		self.send_response(200)
		self.send_headers("Content-type", "application/json")
		if iterations < 10:
			json_string = json.dumps("false")
			self.iterations += 1
		self.wfile.write(bytes(json_string))
		self.end_headers()

def run():
	listen = ("0.0.0.0", 8080)
	server = HTTPServer(listen, myHandler)

	print("listening..")
	server.serve_forever()

run()
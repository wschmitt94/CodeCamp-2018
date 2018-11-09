import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class myHandler(BaseHTTPRequestHandler):

	def do_OPTIONS(self):
		self.send_response(200)
		self.send_header("Access-Control-Allow-Origin", "*")
		self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")
		self.send_header("Access-Control-Allow-Headers", "Content-Type")
		self.end_headers()

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-Type", "application/json")
		self.send_header("Access-Control-Allow-Origin", "*")
		self.end_headers()
		x = {
		"name": "Jake",
		"status": "safe"
		}
		json_string = json.dumps(x);
		print(json_string)
		self.wfile.write(bytes(json_string, "utf-8"))
		

def run():
	listen = ("0.0.0.0", 8080)
	server = HTTPServer(listen, myHandler)

	print("listening..")
	server.serve_forever()

run()
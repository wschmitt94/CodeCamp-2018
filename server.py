import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

myChildren = ['John', 'Jake', 'Mia']

class myHandler(BaseHTTPRequestHandler):

	def getStatus(self, name):
			if name == "Jared":
				return "danger"
			else:
				return "safe"

	def do_OPTIONS(self):
		self.send_response(200)
		self.send_header("Access-Control-Allow-Origin", "*")
		self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")
		self.send_header("Access-Control-Allow-Headers", "Content-Type")
		self.end_headers()

	def do_GET(self):
		if self.path.startswith("/children/"):
			url = self.path.split("/")
			child = url[2]
			self.send_response(200)
			self.send_header("Content-Type", "application/json")
			self.send_header("Access-Control-Allow-Origin", "*")
			self.end_headers()
			child_status = {
			"name": "Not Found",
			"status": ""
			}
			if child in myChildren:
				status = self.getStatus(child)
				child_status = {
				"name": child,
				"status": status
				}
			json_string = json.dumps(child_status);
			self.wfile.write(bytes(json_string, "utf-8"))
		else:
			self.send_response(200)
			self.send_header("Content-Type", "application/json")
			self.send_header("Access-Control-Allow-Origin", "*")
			self.end_headers()
			json_string = json.dumps(myChildren);
			self.wfile.write(bytes(json_string, "utf-8"))

		

def run():
	listen = ("0.0.0.0", 8080)
	server = HTTPServer(listen, myHandler)

	print("listening..")
	server.serve_forever()

run()
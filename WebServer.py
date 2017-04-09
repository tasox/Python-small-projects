#!/usr/bin/python

import SocketServer
import SimpleHTTPServer

class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/admin' :
			self.wfile.write('This page is only for admins!!\n')
			self.wfile.write(self.headers)

		else :
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


httpServer=SocketServer.TCPServer(("",10001),HttpRequestHandler)
httpServer.serve_forever()

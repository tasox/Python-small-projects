#!/usr/bin/python

import SocketServer

#EchoHandler is subclass to SocketServer.BaseRequestHandler
class EchoHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):

		print "Got connection from : "+self.client_address
		data='dummy'
		
		while len(data):
			data=self.request.recv(1024)
			self.request.send(data)

		print "Client left"


#Listen all addresses on port 9000
serverAddr=("0.0.0.0",9000)


#TCPServer or UDPServer
server=SocketServer.TCPServer(serverAddr,EchoHandler)

server.serve_forever	

#!/usr/bin/python

import CGIHTTPServer
import SimpleHTTPServer
import SocketServer

class CGIRequest(CGIHTTPServer.CGIHTTPRequestHandler):
	
	try:
		def do_GET(self):
			CGIHTTPServer.CGIHTTPRequestHandler.do_GET(self)

	except Exception,e:
		print "[-]Error: "+str(e)

try:

	httpServer=SocketServer.TCPServer(("0.0.0.0",80),CGIRequest)
	httpServer.serve_forever

except Exception,t:
	print "[-] Error: "+str(t)

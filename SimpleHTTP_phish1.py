#!/usr/bin/python

##############################################
If the user get into our page automatically
through headers he will download our *.txt.
##############################################
import SocketServer
import SimpleHTTPServer

#SHTTPServer subclass
class SHTTPServer(SimpleHTTPServer.SimpleHTTPRequestHandler):



    def do_GET(self):

         if self.path=='/user':

            self.send_response(200)

            self.send_header('Content-Disposition','attachment;filename=test.txt') 

             self.send_header('Content-Length','100000')

            self.end_headers()



        else : 

             SimpleHTTPServer.SimpleRequestHandler.do_GET(self)


s=SocketServer.TCPServer(("0.0.0.0",9000),SHTTPServer)
s.serve_forever() 

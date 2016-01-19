#!/usr/bin/python

#####################################
#     Simple Chat Server
#Filename: ChatServer.py 
#       Not Multitasking
#####################################

import SocketServer


class Chat(SocketServer.BaseRequestHandler):


    def handle(self):

        print "Got a connection from> ",self.client_address

        data="dummy"

        while len(data): 

             data=self.request.recv(1024) 

             print "Client send> "+data

            self.request.send(data)

         print "Client left"


if __name__=='__main__':

HOST,PORT=("0.0.0.0",8000)
s=SocketServer.TCPServer((HOST,PORT),Chat)
s.serve_forever()




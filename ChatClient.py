#!/usr/bin/python

####################################
#     Simple Client Connection      
#Filename: Client.py     
####################################

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect to Chat Server IP and Port
#change 192.168.1.4 with your IP

s.connect(('192.168.1.4',8000))

while 1:

    userInput=raw_input("Please enter a string: ")

    s.send(userInput)

s.close()

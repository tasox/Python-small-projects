#!/usr/bin/python

################################
#Don't forget to change senderIP 
#           AND
# senderMAC,TargetIP variables
################################

import struct
import socket

#Create Socket for 802.3 ethernet packet

rawSock=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))

rawSock.bind(("eth0",socket.htons(0x0800)))

rawSock=rawSock
HwType="\x00\x01" #Ethernet
ethProtoType="\x08\x06" #ARP
HwSize="\x06"
arpProtoType="\x08\x00" #IPv4
protoSize="\x04"
arpOpcodeReq="\x00\x01" #Request
arpOpcodeRep="\x00\x02" #Reply
senderIP=socket.inet_aton("192.168.1.4")
senderMAC="<YOUR MAC ADDRESS>"
targetIP=socket.inet_aton("192.168.1.3")
targetMAC="\xff\xff\xff\xff\xff\xff"
ether=targetMAC+senderMAC+etherProtoType

#Construct Packet
pkt=struct.pack("!2s2s1s1s2s6s4s6s4s",HwType,arpProtoType,HwSize,protoSize,arpOpcodeReq,senderMAC,senderIP,targetMAC,targetIP)
rawSock.send(eth1+pkt+"Hello there!!!")

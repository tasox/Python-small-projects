#!/usr/bin/python


import sys
from scapy.all import *

ssid=set()

def PacketHandler(pkt):

	dot11_elt=pkt.getlayer(Dot11Elt)
	
	if dot11_elt and (dot11_elt.info not in ssid):
		ssid.add(dot11_elt.info)
		print len(ssid),dot11_elt.info,pkt.addr2

sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler)

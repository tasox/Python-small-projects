#!/usr/bin/python


import sys
from scapy.all import *

ssid=set()

def PacketHandler(pkt):

	dot11_beacon=pkt.getlayer(Dot11Beacon)
	
	if dot11_beacon and (dot11_beacon.info not in ssid):
		ssid.add(dot11_beacon.info)
		print len(ssid),dot11_beacon.info,pkt.addr2,dot11_beacon.name
	

sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler)

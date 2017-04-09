#!/usr/bin/python

import sys
from scapy.all import *


def PacketHandler(pkt):
	
#if pkt.haslayer(Dot11)	
	#print pkt.summary()
	for x in range(len(pkt)):
		if hasattr(pkt[x],"info"):
			print pkt[x].info
		
	return




sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler)

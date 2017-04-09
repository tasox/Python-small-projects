#!/usr/bin/python


import sys
from scapy.all import *

ssid=set()

def PacketHandler(pkt):
	
	probe_req=pkt.getlayer(Dot11ProbeReq)

	if probe_req and (pkt.addr2 not in ssid):
		
		#ssid.add(pkt.addr2)
		#print len(ssid),pkt.addr2
		print probe_req.show()
		wrpcap("ssidfinderv3.cap",pkt)


sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler)

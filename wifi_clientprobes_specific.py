#!/usr/bin/python


import sys
from scapy.all import *


client_mac=sys.argv[2]


def PacketHandler(pkt):


	if pkt.haslayer(Dot11ProbeReq):
		if len(pkt.info) > 0:
			if pkt.addr2 == client_mac: 
			
				print pkt.info

sniff(iface="mon0",count=int(sys.argv[1]),prn=PacketHandler)

		

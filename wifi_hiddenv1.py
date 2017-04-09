#!/usr/bin/python


import sys
from scapy.all import *

ssid_name=set()

def PacketHandler(pkt):

	if pkt.haslayer(Dot11Beacon):
		if not pkt.info:
			if pkt.addr3 not in ssid_name:
				ssid_name.add(pkt.addr3)
				print "HIDDEN SSID with BSSID: ",pkt.addr3
	

	elif pkt.haslayer(Dot11ProbeResp) and (pkt.addr3 in ssid_name) :
			
			print "BSSID %s  WITH SSID %s FOUND!!!: "%(pkt.addr3,pkt.info)


sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler) 

#!/usr/bin/python


import sys
from scapy.all import *

clientprobes=set()

def PacketHandler(pkt):


	if pkt.haslayer(Dot11ProbeReq):
		if len(pkt.info)>0:
			testcase=pkt.info+"-----"+pkt.addr2
			if testcase not in clientprobes:
				clientprobes.add(testcase)
				print "New probe found: "+pkt.addr2+" "+pkt.info

				print "\n------------Probe Table-------------\n"
				counter=1					
				for probes in clientprobes:
					mac,client_ap=probes.split('-----')
					print counter,mac,client_ap
					counter=counter+1
				print "\n-------------Finished-----------------\n"	
					
sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=PacketHandler)

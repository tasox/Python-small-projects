#!/usr/bin/python


import sqlite3,sys
from scapy.all import *


clientprobes=set()
#Connect to the database
connection=sqlite3.connect(sys.argv[1])
connection.execute("CREATE TABLE client_probes(id integer primary key,location char(100) not null,macaddr char(50) not null,probedssid text not null)")

def InsertInDB(client_mac,ssid):
	
	#sys.argv[2] is the location
	connection.execute("insert into client_probes (location,macaddr,probedssid) values (?,?,?)", (sys.argv[2],client_mac,ssid))
	connection.commit()	



def PacketHandler(pkt):


	if pkt.haslayer(Dot11ProbeReq):
		if len(pkt.info)>0:
			testcase=pkt.info+"-----"+pkt.addr2
			if testcase not in clientprobes:
				clientprobes.add(testcase)
				print "New probe found: "+pkt.addr2+" "+pkt.info

				InsertInDB(pkt.addr2,pkt.info)

				print "\n------------Probe Table-------------\n"
				counter=1					
				for probes in clientprobes:
					mac,client_ap=probes.split('-----')
					print counter,mac,client_ap
					counter=counter+1
					
 
				print "\n-------------Finished-----------------\n"	
					
sniff(iface=sys.argv[4],count=int(sys.argv[3]),prn=PacketHandler)

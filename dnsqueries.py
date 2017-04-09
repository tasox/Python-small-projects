#!/usr/bin/python


from scapy.all import *
import sys


rules=('A','AAAA','MX','NS','CNAME')
router_ip='192.168.1.1'
udp=53
dns_array=[]

def PacketHandler(pkt):

	if (pkt.haslayer(DNSQR) and pkt.payload.src not in (router_ip) and pkt.getlayer('DNS').qd):
		
		
		#DNS Query NAME			
		dns_qname=pkt.getlayer('DNS').qd.qname
		#Source IP
		source_ip=pkt.payload.src
		#Source UDP Port
		source_UDPport=pkt.getlayer('UDP').sport
		#add DNS Name to array
		if (dns_qname not in dns_array):
			dns_array.append(dns_qname)

		#Print
		print "Source IP:Port->"+str(source_ip)+":"+str(source_UDPport)+" // Destination:Port ->"+router_ip+":"+str(udp)+" // DNSQR name ->"+str(dns_qname)	
		
			
	
sniff(iface='eth0',count=sys.argv[1],prn=PacketHandler)

#List DNS Queries
print "*"*25+" List DNS Queries "

for x in dns_array:
	print x

print "*"*25+" List DNS Queries "

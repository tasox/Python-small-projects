#!/usr/bin/python

import sys
from scapy.all import *


for ssid in open(sys.argv[1],'r').readlines():
	
	pkt=RadioTap()/Dot11(type=0,subtype=4,addr1=sys.argv[2],addr2="aa:aa:aa:aa:aa:aa",addr3=sys.argv[2])/Dot11ProbeReq()/Dot11Elt(ID=0,info=ssid.strip())/Dot11Elt(ID=1,info="\x02\x04\x0b\x16\x0c\x12\x18\x24")/Dot11Elt(ID=3,info="\x08")

	sendp(pkt,iface="mon0",count=3,inter=.3)


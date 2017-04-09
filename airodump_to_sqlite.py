#!/usr/bin/python

import sqlite3,sys
from bs4 import BeautifulSoup

#Airodump XML file opening
airodumpfile=open(sys.argv[1])
xmlDom=BeautifulSoup(airodumpfile,'lxml')

#Wifi Location
location=sys.argv[3]

#SQLite connection
connection=sqlite3.connect(sys.argv[2])
#Create Table
connection.execute("CREATE TABLE network_table (id integer primary key,location char(100) not null,essid char(255) not null,macaddr char(50) not null,channel int not null,encryption char(255) not null)")

counter=1

networks=xmlDom.findAll('wireless-network')

for network in networks:
	
  	essid=network.find('essid').text
	if not essid:
		essid='--Hidden-essid--'
	bssid=network.find('bssid').text
	channel=network.find('channel').text
	encryption=network.find('encryption').text
	print counter, essid, bssid, channel, encryption
	
	connection.execute("insert into network_table (location,essid,macaddr,channel,encryption) values (?,?,?,?,?)", (location,essid,bssid,channel,encryption))
	#SOS Commit is important!!!!!Without this the sql command will not executed
	connection.commit()
	counter+=1



connection.close()

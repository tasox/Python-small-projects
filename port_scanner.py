@@ -0,0 +1,26 @@
#!/usr/bin/python

import socket

def PortScanner():


	gateway=raw_input("Please print router's gateway!")
	print  "Your gateway is "+str(gateway)
 	
	for port in range(1,1024):

		try:
			socket.setdefaulttimeout(2)

			s=socket.socket()

			s.connect((gateway,port))
	
			#banner=s.recv(1024)

			print '%d:OPEN' %port
			s.close
			
		except: continue
PortScanner()

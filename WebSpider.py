#!/usr/bin/python

import threading
import sys
import mechanize
from bs4 import BeautifulSoup



class WorkerThread(threading.Thread):


	def __init__(self,url):
		threading.Thread.__init__(self)
		self.url=url


	def run(self):
		
		FirstPage=set()
		#uniq=[]
		print "Spidering site "+self.url
		br=mechanize.Browser()
		br.set_handle_robots(False)
		html=BeautifulSoup(br.open(self.url),'lxml')
		for link in br.links():
			if link.text not in FirstPage:
				#uniq.append(link.text)
				FirstPage.add(link.text)
				#plink == parent link
				for plink in FirstPage:
					print "Looking for links inside -> "+plink

					try:
						req=br.click_link(text=plink)
						res=br.open(req)
						for link in br.links():
							print link.text	
					except Exception:
					
						print "Oppssssssss"
					else:
						print res.geturl()



	
#Create thread
new_thread=WorkerThread(str(sys.argv[1]))

#start
new_thread.start()
new_thread.join()

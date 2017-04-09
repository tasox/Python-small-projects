#!/usr/bin/python

import threading
import Queue
import time
import TCPServer


class Test(threading.Thread):

	def __init__(self,num):
		threading.Thread.__init__(self)
		self.num=num


	def run(self):
		print "Hi Tasos...."
		while True:
			counter=self.num.get()
			print "Counter: ",counter
			time.sleep(counter)
			self.q.task_done()
	
class Test2(TCPServer.EchoHandler):
		pass
		
		

q=Queue.Queue()
t=Test2()
t.handle()

for j in range(5):
	print "Create worker thread : ",j
	worker=Test(q)
	worker.setDaemon(True)	
	worker.start()
	print "Worket %d created"%j

for i in range(10):
	q.put(i)

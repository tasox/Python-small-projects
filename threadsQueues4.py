#!/usr/bin/python


import threading
import Queue
import time


class WorkerThread(threading.Thread):

	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.queue=queue
		self.lock=threading.Lock()

	def run(self):
	
		print "Inside Run Function"
		while True:
			self.lock.acquire()
			counter=self.queue.get()
			print "Order to sleep for %d seconds!!!"%counter
			time.sleep(counter)
			self.lock.release()
			print "Finished sleeping for %d seconds"%counter
			
			self.queue.task_done()



queue=Queue.Queue()


for i in range(8):

	print "Creating Worker: %d"%i
	worker=WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "Worker %d Created!!!!"%i

for j in range(8):

	queue.put(j)

queue.join()

print "All Tasks over!!!"

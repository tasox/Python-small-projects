import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections
import datetime
from matplotlib import style
from matplotlib.ticker import MultipleLocator
import time

p = psutil.Process(28180)
print("### PROCESS INFORMATION ")
print("Name: %s" % p.name())
print("PID: %d" %p.pid)
print("Started: %s" % datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S"))
print("Status: %s" %p.status())

style.use('fivethirtyeight')
fig = plt.figure()


# function to update the data
# https://towardsdatascience.com/plotting-live-data-with-matplotlib-d871fac7500b
def animate(i):

    # get data
    mem.popleft()
    # other_bytes (Windows): the number of bytes transferred during operations other than read and write operations.
    mem.append(p.io_counters()[5]/1024)
    
    mem2.popleft()
    # Private memory in KB
    mem2.append(p.memory_info()[11]/1024)    
    
    # clear axis
    ax.cla()
    ax1.cla()
    
    # plot mem
    ax.plot(mem)
    ax.scatter(len(mem)-1, mem[-1])
    ax.text(len(mem)-1.5, mem[-1]+2, "{}%".format(mem[-1]))
    ax.set_xlabel("Memory I/O 'other_bytes' in (KB)")
    ax.set_ylim(0,5000)
    ax.set_xlim(0,10)
    
    # plot memory
    ax1.plot(mem2)
    ax1.scatter(len(mem2)-1, mem2[-1])
    ax1.text(len(mem2)-1, mem2[-1]+2, "{}%".format(mem2[-1]))
    ax1.set_xlabel('Private Memory in (KB)')
    ax1.set_ylim(0,200000)
    ax1.set_xlim(0,10)

    
    
# start collections with zeros
mem = collections.deque(np.zeros(10))
mem2 = collections.deque(np.zeros(10))

# define and adjust figure
#fig = plt.figure(dpi=128,figsize=(12,6), facecolor='#DEDEDE')
ax = plt.subplot(121)
ax1 = plt.subplot(122)
#ax.set_facecolor('#DEDEDE')
#ax1.set_facecolor('#DEDEDE')

# animate
ani = FuncAnimation(fig, animate, interval=2000)
plt.show()

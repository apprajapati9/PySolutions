import time
from collections import deque

#Basic example of how to achieve concurrency without threads in Python from scratch

#deque stands for double ended queue. It is a data structure that allows adding and removing elements from both ends efficiently. Unlike regular queues which are typically operated on using FIFO (first In, First Out) principles, a deque supports both FIFO and LIFO operations.

class Scheduler:
    def __init__(self):
        self.ready = deque() 

    def call_soon(self, func):
        self.ready.append(func) #adds an element to the right end of deque

    def run(self):
        while self.ready:
            func = self.ready.popleft()  #popleft removes and returns an element from the left end of the queue.
            func()
    
sched = Scheduler()
    
def countDown(n):
    if n > 0:
        print('Down', n)
        time.sleep(1)
        sched.call_soon(lambda: countDown(n-1)) 


def countUp(stop, x = 0):
    if x < stop:
        print('Up', x)
        time.sleep(1)
        sched.call_soon(lambda: countUp(stop, x+1))

        
sched.call_soon(lambda: countDown(5)) #appending this func to deque
sched.call_soon(lambda: countUp(5)) #appending this func to deque

#countDown(5) append right and next countUp will be appended right
#and when called takes coundDown() first using popleft.

sched.run()
# countDown(10)                   
# countUp(10)

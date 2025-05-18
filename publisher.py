import zmq, time
from constPS import * #-

import threading
import time

# Function to compute Fibonacci numbers
def compute_fibonacci(s):
    a, b = 0, 1
    i = 0
    
    while True:
        msg = str.encode(f"FIB ({i}) = {a}")
        s.send(msg)
        a, b = b, a + b
        time.sleep(1.5)  # Just to slow it down for visibility
        i += 1

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://"+HOST+":"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
fib_thread = threading.Thread(target=compute_fibonacci, args=(s,))
fib_thread.start()
while True:
	time.sleep(5)                    # wait every 5 seconds
	msg = str.encode("TIME " + time.asctime())
	s.send(msg) # publish the current time
	msg = str.encode("NEWS " + "hello")
	s.send(msg) # publish the current time

# overall synchronization provides us to work on particular method once at a time 
# simialr to work with synchronized keywork in java

import threading
import time

x = 8 
lock = threading.Lock() 

def double_function() : 
    global x, lock 
    lock.acquire() 
    
    while(x < 64) : 
         x *= 2
         print("Double",x)
         time.sleep(2)

    print("Double function executed") 
    lock.release()

def divide_function(): 
    global x , lock
    lock.acquire()

    while(x > 1) : 
        x /= 2 
        print("Divide",x)
        time.sleep(2)

    print("Divide function executed")
    lock.release()

t1 = threading.Thread(target=double_function)
t2 = threading.Thread(target=divide_function)

t1.start()
t2.start()
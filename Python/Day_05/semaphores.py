import threading 
import time

semaphore = threading.BoundedSemaphore(value=4)

def access(thread_number) :
    print(f"{thread_number} is trying to access")
    semaphore.acquire() 
    print(f"================={thread_number} got the access=============") 
    time.sleep(10)
    print(f"{thread_number} completed its work")
    semaphore.release() 

for thread_number in range(1,11): 
    t1 = threading.Thread(target=access, args=(thread_number,))
    t1.start()
    
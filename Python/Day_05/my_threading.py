import threading
import time

def to_walk(dog_name) : 
    time.sleep(5)
    print(f"{dog_name} walking is completed")

def take_out_trash () : 
    time.sleep(2)
    print("You take out the trash")

def get_mail(): 
    time.sleep(2)
    print("Got the mail")

# to_walk()
# take_out_trash()
# get_mail()

# print(f"Finished execution in {time.perf_counter}")

# Creating the thread 

chore1 = threading.Thread(target=to_walk, args=("scooby",)) #inside the args we'll pass the list of tuple 
chore1.start()


chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()


chore1.join()
chore2.join()
chore3.join()


print("All chores are completed")
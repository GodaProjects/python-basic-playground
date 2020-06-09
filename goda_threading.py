import threading
import time
import random


def execute_thread(i):
    print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S")))
    time.sleep(random.randint(1, 4))
    print("Thread {} awake at {}".format(i, time.strftime("%H:%M:%S")))


for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()
    print("Active thread: ", threading.activeCount())
    print("Thread objects: ", threading.enumerate())

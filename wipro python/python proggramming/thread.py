# threading - execution of tasks
# multithreading - execution of many tasks at a time - concurrent execution
# multi processing
# threading - imported
# process - execution unit
# threads - light weight unit inside the process


# simple thread
import threading
import time
def task():
    print("thread started")
    time.sleep(2)
    print("Thread finished")
t = threading.Thread(target=task)
t.start()
t.join()
print("Thread terminated")


# multi threading

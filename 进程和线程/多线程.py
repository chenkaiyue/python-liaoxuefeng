import threading

def loop():
    print "%s is running "% threading.current_thread().name
    ...


print "%s in running" % threading.current_thread().name
t = threading.Thread(target=loop,name="loopthread")
t.start()
t.join()


# -------------锁-----------------
import threading
balance = 0
def change(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    lock = threading.Lock()
    for i in range(1000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()

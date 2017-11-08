#linux 下
import os
pid = os.fork()
if pid == 0:
    print "child process %d %d" % (os.getpid(),os.getpid())
else:
    print "parent process"


#window下

from multiprocessing import Process
import os

def run_proc(name):
    print "run child process %s %s" %(name,os.getpid())

if __name__ == "__main__":
    p = Process(target=run_proc,args=('test',))
    p.start()
    p.join()

# ----------------pool-------------------
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()

if __name__ == "__main__":
    p = Pool(5)
    for i  in range(5):
        p.apply_async(long_time_task,args=(i,))
    p.close()
    p.join()


# ---------------------进程间通信--------------------------
from multiprocessing import Process,Queue
import os

def write(q):
    for value in ['a','b','c']:
        q.put(value)

def read(q):
    while True:
        value = q.get(True)
        print value

if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
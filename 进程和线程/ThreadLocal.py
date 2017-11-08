# 每个线程有自己的局部变量，其他线程不可访问
import threading
local_school = threading.local()

def process_student():
    print" %s in %s"%(local_school.student,threading.current_thread().name)

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=("alice",),name="thread1")
t2 = threading.Thread(target=process_thread,args=("bob",),name="thread2")
t1.start()
t2.start()
t1.join()
t2.join()


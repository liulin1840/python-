# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import threading
import time

def run(n):
    print("task ",n,threading.current_thread())
    time.sleep(2)
    print("task done",n)

start_time = time.time()
t_objs = [] #存线程实例
for i in range(5):
    # 参数是元组,主线程就是程序本身,
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.start()
    t_objs.append(t) #为了不阻塞后面线程的启动，
                     # 不在这里join，先放到一个列表里
#先把他们都放出去,然后统一回来后,主进程再结束
#放出去的时候都要登记一下,
for t in t_objs: #循环线程实例列表，等待所有线程执行完毕
    t.join()     #等待执行结果,等待他回来加入,

#主线程和子线程是并行的,启动一个分支,分支独立运行,程序本身就是一个线程,
print("----------all threads has finished...",threading.current_thread())
print("cost:",time.time() - start_time)
# run("t1")
# run("t2")
#守护线程,等待非守护线程执行完毕才退出,
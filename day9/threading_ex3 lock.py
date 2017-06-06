__author__ = "Alex Li"

import threading
import time
#加法有问题,原因分析: 有1000个线程在执行,gil只有一个线程在执行,
def run(n):
    #lock.acquire()#3.5自己加锁了的,程序变串行了,程序会等10秒,就像排队
    global  num   #一个一个的来,
    num -=1
    time.sleep(0.1)
    #lock.release()


lock = threading.Lock()#声明一个锁的实例,是个全局变量,函数里面可以直接访问

num = 1000

t_objs = []          #存线程实例
for i in range(1000):
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.start()
    t_objs.append(t) #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

# for t in t_objs:  #循环线程实例列表，等待所有线程执行完毕
#     t.join()

print("----------all threads has finished...",threading.current_thread(),threading.active_count())

print("num:",num)
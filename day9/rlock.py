# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import threading, time

#递归锁
def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num


def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)



#一个大门下面两个小门,一共3把锁,
num, num2 = 0, 0
lock = threading.RLock()
for i in range(10):
    t = threading.Thread(target=run3)
    t.start()
#加主线程,一共11个,判断当前的数量,
while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)
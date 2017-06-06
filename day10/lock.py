# -*- coding:utf-8 -*-
__author__ = "Alex Li"

from multiprocessing import Process, Lock

#锁的作用?进程数据独立,屏幕打印
def f(l, i):
    #l.acquire()
    print('hello world', i)
    #l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()
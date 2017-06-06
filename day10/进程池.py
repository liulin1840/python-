# -*- coding:utf-8 -*-
__author__ = "Alex Li"

from  multiprocessing import Process, Pool,freeze_support
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpid())
#回调函数调用前一个函数的执行结果,作为参数
if __name__ == '__main__':#
    #freeze_support()
    pool = Pool(processes=3) #允许进程池同时放入5个进程
    print("主进程",os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)
        #callback=回调,执行完后在去干神马
        #pool.apply(func=Foo, args=(i,)) #串行
        #pool.apply_async(func=Foo, args=(i,)) #串行
    print('end')
    pool.close()
    pool.join()
    #进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。.join()
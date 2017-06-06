# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import time
import queue

#第一次是生成器,下次才会执行
def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield      #这个程序返回,停在这,下次唤醒继续
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)


def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)#给消费者的数据
        con2.send(n)
        time.sleep(1)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()
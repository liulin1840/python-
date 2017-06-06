# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import gevent

def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')
def bar():
    print('Explicit精确的 context内容 to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')
def func3():
    print("running func3 ")
    gevent.sleep(0)
    print("running func3  again ")


gevent.joinall([
    gevent.spawn(foo), #生成，然后切换,遇到sleep就切换
    gevent.spawn(bar),
    gevent.spawn(func3),
])
#自动的切换,有阻塞就换到别的函数去执行
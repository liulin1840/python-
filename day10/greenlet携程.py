# -*- coding:utf-8 -*-
__author__ = "Alex Li"
#封装了的携程,
from greenlet import greenlet
def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()
def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1) #启动一个携程,
gr2 = greenlet(test2)
gr1.switch()          #手动切换,先12 切换到test2 56 再切换34,最后78
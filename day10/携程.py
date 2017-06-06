# -*- coding:utf-8 -*-
__author__ = "Alex Li"
import time

#过来一个请求交给一个函数,
def home():#请求HOME页面
    print("in func 1")
    time.sleep(5) #get data from db 取数据花时间,携程还是串行.要切换
    print("home exec done ")

def bbs():#请求bbs
    print("in func 2")
    time.sleep(2)# 再切换

#遇到IO操作就切换,什么时候又切回去呢?io操作完了就切回去
def login():#请求登录页
    print("in func 3")
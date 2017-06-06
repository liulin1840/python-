# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import time
import threading


event = threading.Event()
# 通过标志位,实现两个线程之间的交互,一个是设定了,一个没有设定,还有个等待设定
# 判断是否设置
def lighter():
    count = 0
    event.set() #先设置绿灯,预先设置标志位
    while True:
        if count >5 and count < 10: #改成红灯
            event.clear() #把标志位清了
            print("\033[41;1 mred light is on....\033[0m")
        elif count >10:
            event.set() #变绿灯
            count = 0
        else:
            print("\033[42;1 mgreen light is on....\033[0m")
        time.sleep(1)
        count +=1
#车先要判断等的颜色,如果设置了标致位,就是绿灯,就起步走,
#否则就是看到了红灯,等一下,等到绿灯,看到绿灯前进,没有设置标致为就卡在那个
#地方,
def car(name):
    while True:
        if event.is_set(): #代表绿灯
            print("[%s] running..."% name )
            time.sleep(1)
        else:
            print("[%s] sees red light , waiting...." %name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)


light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()


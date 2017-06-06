# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import threading, time

#信号量有多把锁,
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)
    # 最多允许5个线程同时运行
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        t.start()
# 效果就是5个5个一起出来
while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
    #print(num)
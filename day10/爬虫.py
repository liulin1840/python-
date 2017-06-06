# -*- coding:utf-8 -*-
__author__ = "Alex Li"

from gevent import monkey;

monkey.patch_all()    #打补丁,把当前程序的io操作做上标记
import gevent         #检测不到urllib的io操作,就会卡,都是串行
from  urllib.request import urlopen
import time

def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()#下载下来的网页
    #f  = open('url.html',"wb")
    #f.write(data)
    # f.close()
    print('%d bytes received from %s.' % (len(data), url))

urls = [ 'https://www.python.org/',
         'https://www.yahoo.com/',
         'https://github.com/'
         ]
#
# time_start = time.time()
# for url in urls:
#     f(url)
# print("同步cost",time.time() - time_start)
#下载一个网页,并发的爬网页,三个携程都执行这个函数
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost",time.time()-async_time_start )
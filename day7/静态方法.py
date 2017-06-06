# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import os
# os.system()
# os.mkdir()

class Dog(object):
    u"""
        这个类是描述狗对象的
    """
    def __init__(self,name):
        self.name = name

    @staticmethod #实际上跟类没什么关系了
    def eat(self):
        print("%s is eating %s" %(self.name,'dd'))

    def talk(self):
        print("%s is talking"% self.name)
d = Dog("ChenRonghua")
d.eat(d)
d.talk()
print d.__doc__
print d.__module__

mod = __import__('lib.aa')
obj = mod.aa.C()
print  (obj.name)

assert type(obj.name) is str
print ('ok')
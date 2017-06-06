# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import os
# os.system()
# os.mkdir()

class Dog(object):
    u'''这个类是描述狗这个对象的'''

    def __init__(self,name,food):
        self.name = name
        self.__food = food

    #@staticmethod #实际上跟类没什么关系了
    #@classmethod
    @property #attribute
    def eat(self):
        print("%s is eating %s" %(self.name,self.__food))
    @eat.setter
    def eat(self,food):
        print("set to food:",food)
        self.__food = food
    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")

    def talk(self):
        print("%s is talking"% self.name)

    def __call__(self, *args, **kwargs):
        print("running call",args,kwargs)

    def __str__(self):
        return "<obj:%s>" %self.name

#print(Dog.__dict__) #打印类里的所有属性，不包括实例属性
d = Dog("miao",u"鱼")
d.eat
d(1,2,3,name='liu')
print(d.__dict__) #打印所有实例属# -*- coding:utf-8 -*-性，不包括类属性
# # d(1,2,3,name=333)
#
# #Dog("ChenRonghua")()
print d #输出类就是输出他的名字
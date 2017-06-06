# -*- coding:utf-8 -*-
__author__ = "Alex Li"

def bulk(self):
    print ("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print ("%s is eating..."%self.name,food)


d = Dog("NiuHanYang")
choice = input(">>:").strip()

# 你输入的是个字符串,我去哪个类里面去找函数,然后再执行
if hasattr(d,choice):
    getattr(d,choice)(u"鱼")#这个的返回值是个地址,要加括号才行
# 如果没有这个函数,那我就设置一个函数来代替
else:
    setattr(d,choice,bulk) #d.talk = bulk,字符串设置
    func = getattr(d, choice)
    func(d)
#set  has? get
print (d.__dict__)
# -*- coding:utf-8 -*-
__author__ = "Alex Li"

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)


#
# d = Dog("NiuHanYang")
# choice = input(">>:").strip()
# getattr(d,choice)



names = ['alex','jack']
# names['sdfsdf']
# data = {}
#
#
try:
    open("tes.txt")

except (KeyError,IndexError) as e :
    print(u"没有这个key",e)
except IndexError as e :
    print(u"列表操作错误",e)
except BaseException as e:
    print(u"未知错误",e)
else:
    print(u"一切正常")
finally:
    print(u"不管有没有错，都执行")
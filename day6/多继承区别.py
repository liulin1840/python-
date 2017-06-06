__author__ = "Alex Li"
#查找顺序,先在自身里面找构造函数,如果没有就去B里面找,按顺序从左到右
#如果B里面没有构造,就去A里面,这里就体现了深度优先的原则
class A:
    #pass
    def __init__(self):
        print("A")
class B(A):
    pass
    # def __init__(self):
    #      print("B")
class C(A):
     #pass
    def __init__(self):
         print("C")
class D(B,C):
    pass
    # def __init__(self):
    #     print("D")


obj = D()
__author__ = "Alex Li"
#����˳��,�������������ҹ��캯��,���û�о�ȥB������,��˳�������
#���B����û�й���,��ȥA����,�����������������ȵ�ԭ��
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
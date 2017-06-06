__author__ = "Alex Li"

from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n\n")


def f(name):
    info('\033[31;1mcalled from child process function f\033[0m')
    print('hello', name)
#这里没有起多进程,在Linux中每个进程有有个父进程来启动,init
if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = Process(target=f, args=('bob',))
    p.start()
    # p.join()
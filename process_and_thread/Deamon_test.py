from threading import Thread
import time

"""
1. 主进程在其代码结束后就已经算运行完毕了(守护进程在此时就被回收)
主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束

2. 主线程在其他非守护线程(non-daemon)运行完毕后才算运行完毕(守护线程在此时就被回收)
因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束
"""


def sayhi(name):
    time.sleep(4)
    print("%s says hi." %name)


def saybye(name):
    time.sleep(2)
    print("%s says bye." % name)


if __name__ == '__main__':
    t1 = Thread(target=sayhi, args=("Crane", ))
    t1.setDaemon(True)
    t1.start()

    t2 = Thread(target=saybye, args=("Crane", ))
    t2.start()

    print("Main thread")
    print(t1.is_alive())
    print(t2.is_alive())

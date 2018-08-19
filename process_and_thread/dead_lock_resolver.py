# 当两个程序同时申请lock的时候，必须要有一个method让步，否则会进入死循环

import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()


def func_1():
    print("func_1 starting.........")

    rst = lock_1.acquire(timeout=2)
    if rst:
        print("func_1 acquires lock 1....")
        lock_1.release()
        print("func_1 releases lock 1")

    else:
        print("func_1 does not have lock 1")

    rst = lock_2.acquire(timeout=2)
    if rst:
        print("func_1 acquires lock 2")
        lock_2.release()
        print("func_1 releases lock 2")
    else:
        print("func_1 does not have lock 2")

    print("func_1 done..........")


def func_2():
    print("func_2 starting.........")
    # get lock 2
    lock_2.acquire()
    print("func_2 acquires lock 2....")
    # sleep for 2 seconds
    time.sleep(2)
    print("func_2 is waiting for lock 1.......")
    # get lock 1
    lock_1.acquire()
    print("func_2 acquires lock 1.......")
    # release lock 1
    lock_1.release()
    print("func_2 releases lock 1")
    # release lock 2
    lock_2.release()
    print("func_2 releases lock 2")

    print("func_2 done..........")


if __name__ == "__main__":
    print("START..............")
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("END..............")

# There are two modules in the python which will give the same function
# to do the multi-threading

# we use threading instead of _thread

import time, threading
from threading import Thread


# Method1 to create the thread
def sayHi(name):
    time.sleep(2)
    print("%s says hello" %name)

if __name__ == '__main__':
    t = Thread(target=sayHi, args=("Crane",))
    t.start()
    print("This is the main thread.")


# Method2 to create the thread
class Sayhi(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    # Must redefine run() method to override the original run() method
    def run(self):
        time.sleep(2)
        print("%s says hello" %self.name)

if __name__ == '__main__':
    t = Sayhi("Crane")
    t.start()
    print("This is the main thread.")


# New threading function block, running after the main thread
# def loop():
#     print("thread %s is running" % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#
#     print("thread %s ends" % threading.current_thread().name)
#
#
# print('thread %s is running' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)

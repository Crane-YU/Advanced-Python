import threading
import time


class MyThread(threading.Thread):
    # override the run() method
    def run(self):
        global num
        time.sleep(1)
        # if get lock
        if mutex.acquire(timeout=1):
            num += num
            msg = self.name + ' set num to ' + str(num)
            print(msg)
            # get the lock again
            mutex.acquire()
            # release all the locks acquired
            mutex.release()
            mutex.release()


num = 0
mutex = threading.RLock()


def loop():
    # Creating five threads
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    loop()
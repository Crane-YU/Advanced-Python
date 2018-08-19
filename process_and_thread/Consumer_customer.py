from threading import Thread
import queue
import threading
import time


class Producer(Thread):
    # override the run() method
    def run(self):
        global q
        count = 0
        # Non-stopping input products into the queue
        while True:
            if q.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = "Produce product number " + str(count)
                    q.put(msg)
                    print(msg)

            time.sleep(0.5)


class Consumer(Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 400:
                for i in range(3):
                    # get是从queue中取出一个值
                    msg = self.name + 'consumes '+ q.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    q = queue.Queue()

    for i in range(500):
        q.put('初始产品'+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
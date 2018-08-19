import threading
import time


def func():
    print("I am running")
    time.sleep(2)
    print("I am done")


if __name__ == "__main__":
    t = threading.Timer(2, func)
    t.start()

    for i in range(10):
        print("{0}.......".format(i))
        time.sleep(1)
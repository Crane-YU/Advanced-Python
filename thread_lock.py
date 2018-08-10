import time, threading

balance = 0
lock = threading.Lock()


def change(n):
    global balance
    # deposit first
    balance = balance + n
    # withdraw second
    balance = balance - n


def run_thread(n):
    # put lock
    lock.acquire()
    try:
        for i in range(100000):
            change(n)
    finally:
        # release lock
        lock.release()
    try:
        for i in range(100000):
            # put lock
            lock.acquire()
            change(n)
    finally:
        # release lock
        lock.release()



t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()

# get the result of the balance
print(balance)

import threading
import time

# The number of threads allowed in the process
number = 3
poll_sema = threading.Semaphore(number)


def func():
    if poll_sema.acquire():
        print(threading.current_thread().getName() + ' get semaphore')
        # waiting for 4s
        time.sleep(4)

        # release semaphore
        poll_sema.release()
        print(threading.current_thread().getName() + " release semaphore")


for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()
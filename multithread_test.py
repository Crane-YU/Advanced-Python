# There are two modules in the python which will give the same function
# to do the multi-threading

# we use threading instead of _thread

import time, threading


# new threading function block, running after the main thread
def loop():
    print("thread %s is running" % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)

    print("thread %s ends" % threading.current_thread().name)


print('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)

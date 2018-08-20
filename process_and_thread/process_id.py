from multiprocessing import Process
import os


def info(title):
    print(title)
    print("Module name: ", __name__)
    # Get parent id
    print("parent process id is ", os.getppid())
    # Get own id
    print("current process id is ", os.getpid())

def f(name):
    info("function f")
    print("hello", name)

if __name__ == '__main__':
    info("main line")
    p = Process(target=f, args=('Bob',))
    p.start()
    p.join()
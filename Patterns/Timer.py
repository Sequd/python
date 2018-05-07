import threading
import time


def hello():
    print("hello, world")


class MyThread(threading.Thread):

    def __init__(self, x):
        self.__x = x
        threading.Thread.__init__(self)

    def run(self):
        # self.start()
        while True:
            print("inner thread 1: %s" % self.__x)
            time.sleep(1)


# create timer
t = threading.Timer(3, hello)
# start thread timer after 3 sec
t.start()

myT = MyThread(121)
myT.start()

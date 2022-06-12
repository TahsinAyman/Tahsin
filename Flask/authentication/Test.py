from os import system as cmd
from threading import Thread
import sys


def thread1():
	sys.path.append('backend')
    cmd("py frontend\\main.py")

def thread2():
	sys.path.append('frontend')
    cmd("py backend\\main.py")

if __name__ == '__main__':
    t1 = Thread(target=thread1)
    t2 = Thread(target=thread2)

    t1.start()
    t2.start()

    thread1()
    thread2()


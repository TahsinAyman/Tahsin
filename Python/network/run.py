from threading import Thread
from os import system as cmd

def py1():
    cmd("py Server.py")

def py2():
    cmd("py Client.py")

if __name__ == '__main__':
    thread1 = Thread(target=py1)
    thread2 = Thread(target=py2)

    py1()
    py2()

    thread1.start()
    thread2.start()

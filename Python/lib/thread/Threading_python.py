from threading import *


class Thread1(Thread):
    def run(self):
        print('Tahsin')


class Thread2(Thread):
    def run(self):
        print('Ayman')


thread1 = Thread1()
thread2 = Thread2()

thread1.run()
thread2.run()

thread1.start()
thread2.start()


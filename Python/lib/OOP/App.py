from abc import ABC, abstractmethod


class App(ABC):
    __inaccessible_i = 2
    i = 3

    @abstractmethod
    def show(self):
        pass

    def call(self):
        print('Call')

    def __str__(self):
        return self.i, self.__inaccessible_i


class App3(ABC):
    __inaccessible_i = 2
    i = 3

    @abstractmethod
    def s(self):
        pass


class App2(App, App3):
    def show(self):
        print('App')

    def s(self):
        print('App3')

    def sh(self):
        print('Ok')


a = App2()
a.show()
a.call()

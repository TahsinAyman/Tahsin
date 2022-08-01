import json

class Person:
    def __init__(self, name=None, age=None):
        self.__name = name
        self._age = age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age 

    def __str__(self):
        return json.loads(obj={"name": self._name, "age": self._age}, indent=4)


if __name__ == '__main__':
    person = Person("Tahsin Ayman", 13)
    person.__name = "Tahsin"
    print(person.__name)

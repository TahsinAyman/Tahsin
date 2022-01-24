class MyList:
    lst = list()
    __doc__ = """This is My Own List"""

    def __init__(self, l):
        self.lst = l

    def append(self, value):
        class_value = str(type(value))[8:-2]
        lst_string = str(self.lst)
        lst_string = lst_string[1: -1]
        lst_string += ', ' + str(value)
        try:
            self.lst = eval(f"[{class_value}(l) for l in lst_string.split(', ')]")
        except ValueError:
            self.lst = []
            print('Invalid Value')
        print(self.lst)
        print(type(self.lst))

    def __str__(self):
        return self.lst


if __name__ == '__main__':
    lst = MyList([input().split()])
       lst.append(int(input()))
    # print(lst)

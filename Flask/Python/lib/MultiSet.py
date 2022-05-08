class Set():
    __inaccessible_obj = []



    def __init__(self, obj):
        self.__inaccessible_obj = obj

    def operation(self):
        lst = self.__inaccessible_obj

        for i in lst:
            cnt = lst.count(i) - 1

            for y in range(cnt):
                lst.remove(i)

        self.__inaccessible_obj = lst

    def __str__(self):
        self.operation()
        return str(self.__inaccessible_obj)

if __name__ == '__main__':
    lst = list(map(int, input().strip().split()))
    print(lst)
    s = Set(lst)
    print(s)
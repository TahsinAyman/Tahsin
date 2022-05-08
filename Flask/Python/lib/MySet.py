from lib.ListInput import *


def my_set(lst):
    l = len(lst)
    for i in lst:
        cnt = False
        for y in range(l):
            if i is lst[y + 1]:
                if not cnt:
                    cnt = True
                    tmp = lst.document(i)
                lst.remove(i)


lst = list_input_integer()
my_set(lst)

print(lst)

<<<<<<< HEAD
def president(n: int, m: int):
    def main(lst: list, m: int, start=0):
        if len(lst) == 1:
            return lst[0]
        cnt = start
        while True:
            cnt += m
            try:
                lst[cnt - 1] = 0
            except Exception:
                s = cnt - len(lst) - m
                for i in lst:
                    if i == 0:
                        lst.remove(0)
                return main(lst, m, s)
=======
<<<<<<< HEAD
def remove_value_from_list(lst, val):
    for v in lst:
        if v == val:
            lst.remove(v)
    return lst


def president(lst: list, m: int, start=0):
    if len(lst) == 1:
        return lst[0]
    cnt = start
    while True:
        cnt += m
        if cnt <= len(lst):
            lst[cnt - 1] = 0
        else:
            s = cnt - len(lst) - m
            return president(remove_value_from_list(lst, 0), m, s)


if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        l = list(map(int, input().strip().split()))
        p = president([_ for _ in range(1, l[0] + 1)], l[1])
        result.append(p)

    for i in result:
        print(i)
=======
def presindent(n, m):
>>>>>>> 83fce1407e27b8b0395040b7ff181f375962ec19
    lst = [i for i in range(1, n+1)]
    return main(lst, m)


if __name__ == '__main__':
<<<<<<< HEAD
    result = []
    for _ in range(int(input())):
        lst = list(map(int, input().strip().split()))
        p = president(lst[0], lst[1])
        result.append(p)

    for i in result:
        print(i)
=======
    presindent(5, 3)
>>>>>>> 160754ab82ef07eb35ef62546fbb05416123465d
>>>>>>> 83fce1407e27b8b0395040b7ff181f375962ec19

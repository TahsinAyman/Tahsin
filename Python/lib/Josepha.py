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
            for v in lst:
                if v == 0:
                    lst.remove(0)
            return president(lst, m, s)


if __name__ == '__main__':
    n = int(input())
    print(president([i for i in range(1, n+1)], 2))

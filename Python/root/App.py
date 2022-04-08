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
    lst = [i for i in range(1, n+1)]
    return main(lst, m)


if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        lst = list(map(int, input().strip().split()))
        p = president(lst[0], lst[1])
        result.append(p)

    for i in result:
        print(i)

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
    lst = [i for i in range(1, n+1)]

    cnt = 0
    while True:
        cnt += 1
        i = lst[cnt-1]

        if cnt == 3:
            cnt = 0

        if len(lst) == 0:
            break

"""
Input Format:
1, 2, 2, 4
3, 3, 3, 3, 3, 3

Output Format:

"""


if __name__ == '__main__':
    presindent(5, 3)
>>>>>>> 160754ab82ef07eb35ef62546fbb05416123465d

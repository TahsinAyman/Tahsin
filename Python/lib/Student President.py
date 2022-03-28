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

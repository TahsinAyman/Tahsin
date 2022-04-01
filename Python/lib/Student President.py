def presidemt(n, m):
    lst = [i for i in range(1, n + 1)]

    cnt = 0
    c = -1
    while True:
        try:
            i = lst[c]  # 5
        except Exception:
            i = lst[0]
        cnt += 1  # 1
        if cnt == 3:  # True
            lst.remove(cnt)
            cnt = 0
        print(lst)  # 1 2 4 5
        c += 1  # 5


if __name__ == "__main__":
    presidemt(5, 3)
    

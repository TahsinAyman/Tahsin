def count(lst, key):
    cnt = 0
    for _ in range(len(lst)):
        for i in lst:
            if i == key:
                cnt = cnt + 1
    return cnt


lst = [int(l) for l in input().split()]
key = int(input())

print(count(lst, key))

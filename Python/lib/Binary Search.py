def search(lst, key):  # 1 2 3 4 5 key: 4
    index = int()
    l = lst
    while True:
        if l[len(lst) // 2] == key:
            index = key
            break
        elif key > l[len(lst) // 2]:
            for i in range(-1, len(l) // 2):
                lst.remove(lst[i])
        elif key < l[len(lst) // 2]:
            for i in range(len(l), -1, -1):
                lst.remove(lst[i])
    return index


lst = [int(l) for l in input().split()]
key = int(input())
print(search(lst, key))

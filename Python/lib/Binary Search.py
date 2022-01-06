<<<<<<< HEAD
def binary_search(lst, key):
    index = int()
    for i in range(len(lst)):
        if lst[i] == key:
            index = i + 1
=======
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
>>>>>>> 036a78242a10c375b39e4d92ad54ccb4434ef6ad
    return index


lst = [int(l) for l in input().split()]
key = int(input())
<<<<<<< HEAD

index = binary_search(lst, key)
print(index)
=======
print(search(lst, key))
>>>>>>> 036a78242a10c375b39e4d92ad54ccb4434ef6ad

def search(lst, key):
    while True:
        mid = len(lst) // 2
        if key == lst[mid]:
            return str(lst[mid]) + " " + str(mid)
        elif key > lst[mid]:
            lst = lst[mid + 1:]
            print(lst)
        elif key < lst[mid]:
            lst = lst[:mid]
            print(lst)
        else:
            return f'{key} Not Found!'


lst = [int(l) for l in input().split()]
key = int(input())
print(search(lst, key))

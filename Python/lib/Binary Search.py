def bubble_sort(lst):
    cnt = 0
    for _ in range(len(lst)):
        cnt += 1
        for i in range(len(lst) - cnt):
            if lst[i] > lst[i + 1]:
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp


def search(lst, key):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == key:
            return mid
        elif key > lst[mid]:
            low = mid + 1
        elif key < lst[mid]:
            high = mid - 1
    return -1


lst = [int(l) for l in input().split()]
bubble_sort(lst)
print(lst)
key = int(input())
print(search(lst, key))

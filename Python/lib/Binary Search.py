from lib.BubbleSort import bubble_sort


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
    return f"{key} not Found."


lst = [int(l) for l in input().split()]
bubble_sort(lst)
print(lst)
key = int(input())
print(search(lst, key))

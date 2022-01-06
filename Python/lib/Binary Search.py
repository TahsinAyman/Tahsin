def binary_search(lst, key):
    index = int()
    for i in range(len(lst)):
        if lst[i] == key:
            index = i + 1
    return index


lst = [int(l) for l in input().split()]
key = int(input())

index = binary_search(lst, key)
print(index)

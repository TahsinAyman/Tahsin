def bubble_sort(lst):
    cnt = 0
    for _ in range(len(lst)):
        cnt += 1
        for i in range(len(lst) - cnt):
            if lst[i] > lst[i + 1]:
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp


lst = [int(l) for l in input().split()]
bubble_sort(lst)
print(lst)

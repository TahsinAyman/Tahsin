def rotLeft(lst, d):
    num = int()

    for _ in range(d):
        num = lst[0]
        lst.remove(num)
        lst.insert(len(lst), num)

    return lst


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
lst = list(map(int, input().rstrip().split()))

print(rotLeft(lst, d))

number = [int(l) for l in input().strip().split()]
n, m, number, request = number[0], number[1], [], []

for i in range(n):
    number.append(int(input()))

for i in range(m):
    request.append([int(l) for l in input().split()])

for r in request:
    if r[0] == 0:
        print('No entry' if r[1] > n - 1 else number[r[1]])
    elif r[0] == 1:
        if r[1] > n - 1:
            print('No entry')
        else:
            number.remove(number[r[1]])
            number.insert(r[1], r[2])
            print('New number for', r[1], 'is', r[2])

r, number, request = [int(_) for _ in input().strip().split()], [], []
for i in range(r[0] + r[1]):
    number.append(int(input())) if i < r[0] else request.append([int(_) for _ in input().strip().split()])
for y in request:
    if y[0] == 0:
        print('No entry' if y[1] > r[0] - 1 else number[y[1]])
    elif y[0] == 1:
        if y[1] > r[0] - 1:
            print('No entry')
        else:
            number.remove(number[y[1]])
            number.insert(y[1], y[2])
            print('New number for', y[1], 'is', y[2])
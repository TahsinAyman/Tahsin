number = [int(l) for l in input().strip().split()]  # List Input.
n, m, number, id = number[0], number[1], [], []  # Defining Values.
for i in range(n + m):
     id.append(int(input())) if i >= n else number.append(int(input()))  # Short id else
for z in id:
    print('No entry' if z > n - 1 else number[z])  # Short if else

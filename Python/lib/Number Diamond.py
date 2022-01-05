"""
Input: 5

        0
      1 2 3
    4 5 6 7 8
  9 0 1 2 3 4 5
6 7 8 9 0 1
     1 2 3
       4
"""
n = int(input('Enter the Value of Numerical Diamond: '))
cnt = -1

for i in range(n):
    for y in range(n - 1, i, -1):
        print('  ', end='')
    for z in range(i * 2 + 1):
        cnt = cnt + 1
        if cnt > 9:
            cnt = 0
        print(cnt, end=' ')
    print()

for i in range(n - 1, 0, -1):
    for y in range(i, n):
        print('  ', end='')
    for z in range(i * 2 - 1, 0, -1):
        cnt = cnt + 1
        if cnt > 9:
            cnt = 0
        print(cnt, end=' ')
    print()

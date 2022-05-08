lst = []
for _ in range(list(map(int, input().strip().split()))[0]):
    lst.append(list(map(int, input().strip().split())))
print()
for i in range(len(lst)):
    for y in range(len(lst[i])):
        if lst[i][y] == 0:
            lst[i][y] = ' '
        elif lst[i][y] == 1:
            lst[i][y] = '#'
        elif lst[i][y] == 2:
            lst[i][y] = '|'
            try:
                lst[i-1][y] = '*'
            except Exception:
                pass
            try:
                lst[i-1][y+1] = '*'
            except Exception:
                pass
            try:
                lst[i-1][y+2] = '*'
            except Exception:
                pass
            try:
                lst[i-1][y-1] = '*'
            except Exception:
                pass
            try:
                lst[i-1][y-2] = '*'
            except Exception:
                pass
            try:
                lst[i-2][y] = '*'
            except Exception:
                pass
            try:
                lst[i-2][y+1] = '*'
            except Exception:
                pass
            try:
                lst[i-2][y-1] = '*'
            except Exception:
                pass
            try:
                lst[i-3][y] = '*'
            except Exception:
                pass
        elif lst[i][y] == 3:
            lst[i][y] = '_'
            try:
                lst[i-1][y] = '_'
            except Exception:
                pass
            try:
                lst[i-2][y] = '_'
            except Exception:
                pass
            try:
                lst[i][y-1] = '|'
            except Exception:
                pass
            try:
                lst[i][y+1] = '|'
            except Exception:
                pass
            try:
                lst[i-1][y+1] = '\\'
            except Exception:
                pass
            try:
                lst[i-1][y-1] = '/'
            except Exception:
                pass

for i in lst:
    for y in i:
        print(y, end='')
    print()

"""
Input Format:
1, 2, 2, 4
3, 3, 3, 3, 3, 3
1, 3, 2, 2

Output Format:
3
4
2
"""

lst = list(map(int, input().strip().split(',')))

uber = 0

for i in lst:
    if i == 4:
        uber += 1
    else:
        is_true = False
        for y in lst:
            if y == 4 - i:
                lst.remove(y)
                is_true = True
                uber += 1
        if not is_true:
            uber += 1
print(uber)

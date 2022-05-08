"""
Input Format
3 3
1 2 3
4 5 6
7 8 9
"""

"""
Output Format
1 2 3 = 6
4 5 6 = 15
7 8 9 = 24
===
"""
lst = []
r = list(map(int, input().strip().split()))
row_size, col_size = r[0], r[1]
del r

for _ in range(row_size):
	lst.append(list(map(int, input().strip().split())))

print(lst)
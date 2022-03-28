"""
Input Format
3 3                                                                                                                                   
1 2 3                                                                                                                                 
4 5 6                                                                                                                                 
7 8 9

Output Format
45
15
15
"""

lst = []
r = list(map(int, input().strip().split()))
for _ in range(r[0]):
	lst.append(list(map(int, input().strip().split())))



sum = 0
for i in lst:
	for y in i:
		sum += y  
print(sum)

cnt = 0
sum = 0
for i in lst:
	sum += i[cnt]
	cnt += 1
print(sum)

cnt = len(lst)


"""
Input Format:
1, 2, 2, 4

Output Format:
3
"""


lst = list(map(int, input().strip().split(',')))

uber = 0

sum = 0
for i in lst:
    sum += i

uber = sum / len(lst)

u = str(uber)
index = None
for i in range(len(u)):
    if u[i] == '.':
        index = i
        break

if int(u[index + 1:]) > 0:
    uber = int(u[:index]) + 1
else:
    uber = int(u[:index])

print(uber)

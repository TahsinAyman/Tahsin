result = []

for _ in range(int(input())):
	string = input().split()

	if string[1] in string[0]:
		result.append('Yes')
	else:
		result.append("No")

for i in result:
	print(i)

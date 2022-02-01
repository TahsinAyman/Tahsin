dic = dict()

for _ in range(int(input())):
    lst = input().split()
    dic[lst[0]] = lst[1]

print('lex = {')
for i in dic:
    print(f'    "{i}": "{dic[i]}",' if i != list(dic.keys())[-1] else f'    "{i}": "{dic[i]}"')
print('}')
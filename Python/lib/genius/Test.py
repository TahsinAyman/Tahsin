dic = dict()

for _ in range(int(input())):
    lst = input().split()
    dic[lst[0]] = lst[1]

print('lex = {')
for i in dic:
    if i != list(dic.keys())[-1]:
        print(f'"{i}": "{dic[i]}",')
    else:
        print(f'"{i}": "{dic[i]}"')
print('}')

dic = dict()

for _ in range(int(input())):
    lst = input().split()
    dic[lst[0]] = lst[1]

print('lex = {')
for k, v in dic.items():
    if k != list(dic.keys())[-1]:
        print(f'    "{k}": "{v}", ')
    else:
        print(f'    "{k}": "{v}"')
print('}')

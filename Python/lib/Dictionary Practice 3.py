dic = dict()

for _ in range(int(input())):
    lst = input().split()
    dic[lst[0]] = lst[1]

print('lex = {')
for i in range(len(dic)):
    if i != len(dic) - 1:
        print(f'"{list(dic.keys())[i]}": "{list(dic.values())[i]}",')
    else:
        print(f'"{list(dic.keys())[i]}": "{list(dic.values())[i]}"')
print('}')

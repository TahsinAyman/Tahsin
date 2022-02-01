dic = dict()

for _ in range(int(input())):
    lst = input().split()
    dic[lst[0]] = lst[1]

print('lex = {')
<<<<<<< HEAD
for i in dic:
    print(f'    "{i}": "{dic[i]}",' if i != list(dic.keys())[-1] else f'    "{i}": "{dic[i]}"')
print('}')
=======
<<<<<<< HEAD
for i in dic:
    if i != list(dic.keys())[-1]:
        print(f'"{i}": "{dic[i]}",')
    else:
        print(f'"{i}": "{dic[i]}"')
=======
for i in range(len(dic)):
    if i != len(dic) - 1:
        print(f'"{list(dic.keys())[i]}": "{list(dic.values())[i]}",')
    else:
        print(f'"{list(dic.keys())[i]}": "{list(dic.values())[i]}"')
>>>>>>> 76213853b37b973d9321ec4d435ef5afb92c85d0
print('}')
>>>>>>> 2c730a6a345bef0d6c3e7f65a3e53e96b8c833a7

n = int(input())
result = []
command = str()

for _ in range(n):
    lst = [input('>: ').split()]
    command = lst[0]
    lst.remove(lst[0])
    if command == 'append':
        for i in lst:
            result.append(int(i))
    elif command == 'sort':
        eval(f'result.{command}()')  # result.sort()
    elif command == 'print':
        print(result)
    elif command == 'insert':
        eval(f'result.{command}({lst[0]}, {lst[1]})')
    elif command == 'count':
        print(len(result))
    elif command == 'remove':
        eval(f'result.{command}(result[{lst[1]}])')
    else:
        print('Wrong Command')

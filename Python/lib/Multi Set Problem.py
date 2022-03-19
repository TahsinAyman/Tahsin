"""
Input Format

10
append 3 2 1
print
insert 0 2
print
remove 0
print
sort <
print
sort >
print
"""

"""
Output Format

[
    [3, 2, 1],
    [2, 3, 2, 1],
    [3, 2, 1],
    [1, 2, 3],
    [3, 2, 1]
]
"""
result = []
lst = []

for _ in range(int(input())):
    string = input().strip().split()
    command = string[0]
    string.remove(string[0])
    try:
        number = list(map(int, string))
    except Exception:
        number = string[0]

    if command == 'append':
        for i in number:
            lst.append(i)
    elif command == 'insert':
        lst.insert(number[0], number[1])
    elif command == 'remove':
        lst.remove(lst[number[0]])
    elif command == 'sort':
        if number == '>':
            lst.sort(reverse=True)
        elif number == '<':
            lst.sort()
    elif command == 'print':
        print(lst)
        result.append(lst)
    else:
        print("Wrong Command")

if not result:
    pass
else:
    print(result)
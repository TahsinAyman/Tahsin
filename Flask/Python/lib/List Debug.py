"""
Sample Input:
10
append 1 2 3
print
remove 1
insert 0 5
print
pop 0
insert 0 6
print
sort
print

Sample Output:
[
    [1, 2, 3],
    [5, 2, 3],
    [6, 2, 3],
    [2, 3, 6]
                ]
"""
result = []
ls = []
for _ in range(int(input())):
    l = ls
    string = input().strip().split()
    command = string[0]
    string.pop(0)
    lst = list(map(int, string))

    if command == 'append':
        for i in lst:
            l.append(i)
    elif command == 'insert':
        l.insert(lst[0], lst[1])
    elif command == 'remove':
        l.remove(lst[0])
    elif command == 'pop':
        l.pop(lst[0])
    elif command == 'sort':
        l.sort()
    elif command == 'print':
        result.append(l)

for i in result:
    print(i)

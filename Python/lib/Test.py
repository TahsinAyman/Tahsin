# Older version

def old():
    var2 = int()
    var1 = int(input('Enter the Number: '))

    if var1 == 0:
        exit('Bye Noobs')

    while True:
        var2 = int(input('Enter the Number: '))
        if var2 == 0:
            print(var1)
            break
        var1 = var1 + var2


# Newer version which everyone use

def new_version():
    lst = [int(l) for l in input().split(' + ')]
    sum = 0
    for i in lst:
        sum = sum + i

    print(sum)


print('1. Old Version')
print('2. Newer Version')
choice = int(input('Enter choice: '))

if choice == 1:
    old()
elif choice == 2:
    new_version()

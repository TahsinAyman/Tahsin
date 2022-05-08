list_size = int(input('Enter the Size of List: '))
a = []

for i in range(list_size):
    a.append(int(input('Enter Data: ')))

print(a)

output = 0

for i in range(0, len(a), 1):
    output = output + a[i]

print('[Result =', output, ']')

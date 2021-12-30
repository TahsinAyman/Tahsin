n = int(input('Enter the size of Box: '))

print('╔', end=' ')
for top in range(1, (n // 2) + 2):
    print('═', end=' ')
print('╗')

for row in range(1, (n // 2) + 2):
    print('║', end='')
    for col in range(1, (n // 2) + 2):
        print('  ', end='')
    print(' ║', end='')
    print()

print('╚', end=' ')
for bottom in range(1, (n // 2) + 2):
    print('═', end=' ')
print('╝', end=' ')

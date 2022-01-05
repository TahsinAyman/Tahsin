n = int(input('Enter the Size of Box: '))

print('╔', end=' ')
print('═ ' * ((n // 2) + 1), end='')
print('╗')
for row in range((n // 2) + 1):
    print('║', end=' ')
    print('  ' * ((n // 2) + 1), end='')
    print('║')
print('╚', end=' ')
print('═ ' * ((n // 2) + 1), end='')
print('╝', end='')

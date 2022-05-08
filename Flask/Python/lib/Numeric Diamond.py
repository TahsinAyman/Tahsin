# Decoration Please do not consider this as lines of code (:
# Start
import time

# End
# Actual code Start

n = int(input('Enter the Value of Diamond: '))
cnt = -1

for top in range(n):
    for _ in range(n - 1, top, -1):
        print('  ', end='')
    for _ in range(top * 2 + 1):
        cnt += 1
        if cnt > 9:
            cnt = 0
        print(cnt, end=' ')
    print()

for bottom in range(n - 1, 0, -1):
    for _ in range(bottom, n):
        print('  ', end='')
    for _ in range(bottom * 2 - 1):
        cnt += 1
        if cnt > 9:
            cnt = 0
        print(cnt, end=' ')
    print()
# Actual Code End
# Took 22 lines.

# Decoration Please do not consider this as lines of code (:
# Start
print('______________________\n\t', end='')
for ch in 'Thank You':
    print(ch, end='')
    time.sleep(0.50)  # Adding some delay to decorate
# End
# Coded By Tahsin Ayman

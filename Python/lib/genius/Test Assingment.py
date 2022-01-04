'''
n = 3
  0
 123
45678
 901
  2

n = 4
   0
  123
 45678
9012345
 67890
  123
   4

n = 3
*****
 ***
  *
n = 4
*******
 *****
  ***
   *
'''
# x = int(input(" enter some int ."))
# for row in range(x):
#     for i in range(row, x - 1):
#         print(" ", end=" ")
#     for i in range(row + 1):
#         print("*", end=" ")
#     print('* ' * row)

# n = 7  # int(input('Enter value of Pyramid: '))
# for i in range(n):
#     print('  ' * (n - i - 1) + '* ' * (i * 2 + 1))


lst = [int(l) for l in input('Enter Numbers: ').split()]
print(lst)
sum = 0
for i in lst:
    sum += i
print('Result = ', sum)


<<<<<<< HEAD
# oct_str = ''''''

#
# print(oct_str)
def print_formatted(number):
    w = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(w, ' '), oct(i)[2:].rjust(w, ' '), hex(i).upper()[2:].rjust(w, ' '),
              bin(i)[2:].rjust(w, ' '))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
=======
from numpy import *

var2 = array([1, 1, 1], int)
var1 = array([1, 2, 3], int)

print(subtract(var1, var2))
>>>>>>> ae7121c6a8873595ee95beec9484ea5b8a6dbed3

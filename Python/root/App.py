<<<<<<< HEAD
from os import system as cmd

lst = []
for _ in range(list(map(int, input().strip().split()))[0]):
    lst.append(list(map(int, input().strip().split())))
# cmd('cls')

print_stuff = []

# lst[3][5] = '*'
#
# for i in lst:
#     for y in i:
#         print(y, end=' ')
#     print()
for i in range(len(lst)):
    for y in range(len(lst[i])):
        if lst[i][y] == 0:
            lst[i][y] = ' '
        elif lst[i][y] == 1:
            lst[i][y] = '#'

for i in range(len(lst)):
    for y in range(len(lst[i])):
        if lst[i][y] == 2:
            lst[i][y] = '|'
            try:
                lst[i-1][y] = '*'
            except Exception:
                pass
            try:
                lst[i-1][y+1] = '*'
            except Exception:
                pass
            try:
                lst[i-1][y+2] = '*'
            except Exception:
                pass
            try:
                lst[i-1][y-1] = '*'
            except Exception:
                pass
            try:
                lst[i-1][y-2] = '*'
            except Exception:
                pass
            try:
                lst[i-2][y] = '*'
            except Exception:
                pass
            try:
                lst[i-2][y+1] = '*'
            except Exception:
                pass
            try:
                lst[i-2][y-1] = '*'
            except Exception:
                pass
            try:
                lst[i-3][y] = '*'
            except Exception:
                pass
        if lst[i][y] == 3:
            lst[i][y] = '_'
            try:
                lst[i-1][y] = '_'
            except Exception:
                pass
            try:
                lst[i-2][y] = '_'
            except Exception:
                pass
            try:
                lst[i][y-1] = '|'
            except Exception:
                pass
            try:
                lst[i][y+1] = '|'
            except Exception:
                pass
            try:
                lst[i-1][y+1] = '\\'
            except Exception:
                pass
            try:
                lst[i-1][y-1] = '/'
            except Exception:
                pass

for i in lst:
    for y in i:
        print(y, end=' ')
    print()

for i in print_stuff:
    print(i)
=======
class App:
    @staticmethod
    def main(args=[]):
        print("This is A Sample Programmm At Sublime Text")


if __name__ == '__main__':
    import sys

    App.main(sys.argv[1:])
>>>>>>> 160754ab82ef07eb35ef62546fbb05416123465d

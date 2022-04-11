<<<<<<< HEAD
def president(n: int, m: int):
    def main(lst: list, m: int, start=0):
        if len(lst) == 1:
            return lst[0]
        cnt = start
        while True:
            cnt += m
            try:
                lst[cnt - 1] = 0
            except Exception:
                s = cnt - len(lst) - m
                for i in lst:
                    if i == 0:
                        lst.remove(0)
                return main(lst, m, s)
    lst = [i for i in range(1, n+1)]
    return main(lst, m)
=======
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
>>>>>>> 83fce1407e27b8b0395040b7ff181f375962ec19


if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        lst = list(map(int, input().strip().split()))
        p = president(lst[0], lst[1])
        result.append(p)

<<<<<<< HEAD
    for i in result:
        print(i)
=======
    App.main(sys.argv[1:])
>>>>>>> 160754ab82ef07eb35ef62546fbb05416123465d
>>>>>>> 83fce1407e27b8b0395040b7ff181f375962ec19

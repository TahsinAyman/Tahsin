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

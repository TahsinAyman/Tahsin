def is_paranoid(number):
    reversed_num = ''
    for i in range(len(str(number)) - 1, -1, -1):
        reversed_num += str(number)[i]
    if str(number) == reversed_num:
        return "true"
    else:
        return "false"



if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        lst.append(int(input()))
    for i in lst:
        print(is_paranoid(i))


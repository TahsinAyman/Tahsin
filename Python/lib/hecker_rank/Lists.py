if __name__ == '__main__':
    # N = int(input())
    lst = []
    insert_num = []
    inputStr = input().split()

    for i in inputStr:
        insert_num.append(int(i))

    append = inputStr[0]

    if append == 'append':
        lst.append(int(insert_num))
    print(lst)

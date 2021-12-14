if __name__ == '__main__':
    # N = int(input())
    lst = []
    insert_num = []
    append, insert_num = input().split()
    if append == 'append':
        lst.append(int(insert_num))
    print(lst)

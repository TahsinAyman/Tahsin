if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    second_max = maxint = -1000
    for i in arr:
        if i > maxint:
            second_max = maxint
            maxint = i
        elif second_max < i != maxint:
            second_max = i
    print(second_max)

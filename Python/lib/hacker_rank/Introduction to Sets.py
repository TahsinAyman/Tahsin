def average(array):
    array = set(array)
    sum = 0
    for i in array:
        sum = sum + i
    result = float(sum / len(array))
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

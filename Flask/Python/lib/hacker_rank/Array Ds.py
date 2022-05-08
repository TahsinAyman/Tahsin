# Complete the 'reversed_array' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reversed_array(lst: list):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result


if __name__ == '__main__':
    lst = list(map(int, input().strip().split()))
    print(reversed_array(lst))
    
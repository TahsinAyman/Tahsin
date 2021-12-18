import numpy


def arrays(arr):
    arr.reverse()
    result = numpy.array(arr, float)
    return result


arr = input().strip().split(' ')
result = arrays(arr)
print(result)

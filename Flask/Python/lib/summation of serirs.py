def summation_of_series(n):
    if n <= 1:
        return n
    return n + summation_of_series(n - 1)


print(summation_of_series(0))

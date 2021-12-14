from calendar import isleap


def is_leap(year):
    leap = False
    yy = year % 100
    print(yy)
    if year % 400 == 0:
        leap = True
        if year % 100 != 0:
            leap = False
        if yy % 4 == 0:
            leap = True
    return leap


year = int(input())
print(isleap(year))

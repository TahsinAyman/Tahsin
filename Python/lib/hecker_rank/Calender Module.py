import calendar

lst = list(input().split())
lst.reverse()
print(calendar.day_name[calendar.weekday(lst[0], lst[1], lst[2])])

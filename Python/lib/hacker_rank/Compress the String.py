string = input()
lst = []

for ch in string:
    lst.append(string.count(ch))
    string.replace(ch, '')

print(lst)

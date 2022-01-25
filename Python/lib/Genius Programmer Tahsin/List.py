# lines = int(input("Enter how many lines: "))
lst = []
cnt = 0
while True:
    txt = input().split()
    for x in txt:
        lst.append(x)
print(lst)

search = input('Enter the Value to Search: ')
for y in lst:
    if search.upper() == y.upper():
        cnt += 1
print(cnt)
# Tahsin Test 2

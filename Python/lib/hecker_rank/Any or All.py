n = input()
lst = [int(inputStr) for inputStr in input().split()]
bul = False
for i in lst:
    if i >= 0:
        bul = True
palen = ""
for i in range(len(n)-1, -1, -1): palen += n[i]
print('True' if lst == palen and bul else 'False')

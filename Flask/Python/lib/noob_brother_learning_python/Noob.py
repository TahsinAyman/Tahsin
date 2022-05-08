output = []

while True:
    a = 0
    s = input().replace(' ', '')
    if len(s) > 0:
        for i in s:
            if a < 0:
                break
            if i == '[':
                a += 1
            elif i == ']':
                a -= 1
        if a == 0:
            output.append('Yes')
        else:
            output.append('No')
    else:
        break
for i in output:
    print(i)

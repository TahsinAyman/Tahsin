text = []
while True:
    txt = input().lower()
    if len(txt) > 0:
        text.append(txt)
    else:
        break
text.sort()
for i in text:
    print(i)

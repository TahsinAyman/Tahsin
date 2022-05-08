from email import utils

lst = []

for _ in range(int(input())):
    mail = input()
    lst.append(mail)

for i in lst:
    for y in i:
        if not y.isalpha():
            continue
        else:
            print(utils.parseaddr(mail))

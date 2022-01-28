student_vote = []
dic = dict()

for _ in range(int(input())):
    student_vote.append(int(input()))

for i in student_vote:
    if i == 0:
        pass
    else:
        try:
            if dic[i] > 0:
                dic[i] += 1
        except Exception:
            dic[i] = 1

max = 0
cnt = 0
win = ''
for x in dic:
    x = dic[x]
    if x > max:
        max = x
for k in dic:
    k = dic[k]
    if k is max:
        cnt += 1
try:
    if cnt > 1:
        win = 'No Winner!'
    elif max >= len(student_vote) // 2:
        win = 'Majority win'
    elif max >= len(student_vote) // 3:
        win = 'Minority win'
    else:
        win = 'No Winner!'
except KeyError:
    pass

print(win if win == 'No Winner!' else f'{win}\n{list(dic.keys())[list(dic.values()).index(max)]}')
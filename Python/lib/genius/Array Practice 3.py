dic, student_vote, max, cnt, win = dict(), [], 0, 0, ''
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
if win == 'No Winner!':
    print(win)
else:
    print(win)
    print(list(dic.keys())[list(dic.values()).index(max)])

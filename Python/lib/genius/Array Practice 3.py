student_vote = []

for _ in range(int(input())):
    student_vote.append(int(input()))

for i in student_vote:
    cnt = 0
    for y in student_vote:
        if i == y:
            cnt += 1

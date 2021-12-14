limit = int(input())
student_marks = {}
for i in range(limit):
    name, marks = str(input()).split(), list(input())
    student_marks.update({name: marks})
query_name = str(input('Enter the name to see their information: '))
sum = 0
average = 0
for i in student_marks[query_name]:
    sum = sum + i
    average = "{0:.2f}".format(sum / len(student_marks[query_name]))
print(average)

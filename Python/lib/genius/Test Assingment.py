number = [int(l) for l in input().split()]  # The First Line Input.
n, m, number, id = number[0], number[1], [], []  # Defining Values.
for i in range(number[0]):
    number.append(int(input()))  # Number List Appending The Employee Number.
for y in range(number[1]):
    id.append(int(input()))  # ID List Appending The ID Number of Employee.
for z in id:
    if z > number[0] - 1:  # Checking if There is an IndexError Exception (An Error in to compile time).
        print('No entry')  # Run if There is An Error.
    else:  # if There is an Error Then:
        print(number[z])  # Run if Index is Right.
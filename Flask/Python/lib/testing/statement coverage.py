def statementCoverage(i, j, k):
    if i > 0:
        if j > 10:
            while k > 10:
                print('Task 1')
                k -= 1
        print('Task 2')
    print('End of task')
    print()


def statementCoverage2(i, j, k):
    if i > 0:
        if j > 10:
            while k > 10:
                print('Task 1')
                k -= 1
        else:
            print('Task 2')

    print('End of task')
    print()


statementCoverage(1, 11, 11)

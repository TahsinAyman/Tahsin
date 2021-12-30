# x = 7
# for i in range(1, x):
#     for ex in range(i, x):
#         print(ex, end=" ")
#
#     for ex in range(i):
#         print("*", end=" ")
#
#     for ex in range(i-1):
#         print("*", end=" ")
#     print()
# for i in range(x):
#     for ex in range(i):
#         print(ex, end=" ")
#
#     for ex in range(i, x):
#         print("*", end=" ")
#
#     for ex in range(i, x -1):
#         print("*", end=" ")
#     print()


mid = 3
midEnd = midStart = mid
for row in range(1, mid * 2):
    if row <= mid:
        midEnd -= 1
        midStart += 1
    else:
        midEnd += 1
        midStart -= 1

    for col in range(mid * 2):
        print("*" if (midEnd < col < midStart) else " ", end=" ")

    print()

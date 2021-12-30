print("1.stairs")
print("2.pyramid")
print("3.ulta stairs")
print("4.stars")
choice = int(input(""))
x = int(input("how much shit???"))

if choice == 1:
    for i in range(x):
        for ex in range(i + 1):
            print("*", end=" ")
        print("")



elif choice == 2:
    for i in range(x):
        for ex in range(i, x):
            print(" ", end=" ")

        for ex in range(i + 1):
            print("*", end=" ")

        for ex in range(i):
            print("*", end=" ")
        print("")



elif choice == 3:
    for i in range(x):
        for ex in range(i, x):
            print(" ", end=(" "))

        for ex in range(i + 1):
            print("*", end=" ")
        print("")



elif choice == 4:
    for i in range(x):
        for ex in range(i, x):
            print(" ", end=" ")

        for ex in range(i):
            print("*", end=" ")

        for ex in range(i - 1):
            print("*", end=" ")
        print()
    for i in range(x):
        for ex in range(i):
            print(" ", end=" ")

        for ex in range(i, x):
            print("*", end=" ")

        for ex in range(i, x - 1):
            print("*", end=" ")
        print()

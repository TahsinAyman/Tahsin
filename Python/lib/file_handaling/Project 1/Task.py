# This is a Small Task For Adding 2 values.
# Example:
# 2 integer 1 and 2
# Prints 3
# Explanation 1 + 2 = 3
# Constrains: 1 >= a >= 10, 1 >= b >= 10
def ishaan_code(main_array):
    Range = [int(do) for do in input("e.g. 5 3").strip().split(" ")]
    search = []
    for i in range(Range[0]):
        main_array.append(int(input("numbers")))
    for z in range(Range[1]):
        search.append(int(input("position to search")))
    for IO in range(len(search)):
        if search[IO] > len(main_array):
            return "No Entry!!!!!"
        else:
            return main_array[search[IO]]

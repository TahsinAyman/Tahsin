from MultiSet import MyList

# Sample Input
"""
6
append 1 2
print
insert 1 3
print
remove 3
print
"""
# Sample Output
"""
[
    [1, 2],
    [1, 3, 2],
    [1, 2]
]
"""

multi_set = MyList()
result = []

for _ in range(int(input())):
    nums = input().split()
    command = nums[0]
    nums.remove(nums[0])

    if command == 'append':
        for i in nums:
            multi_set.add(int(i))
    if command == 'insert':
        multi_set.add(int(nums[1]), int(nums[0]))
    if command == 'remove':
        multi_set.remove(int(nums[0]))
    elif command == 'print':
        result.append(multi_set.__str__())

print('[')
for i in range(len(result)):
    print('\t' + result[i] if i == len(result) - 1 else '\t' + result[i] + ',')
print(']')

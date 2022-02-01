tom = [int(_) for _ in input().strip().split()]
jerry = [int(_) for _ in input().strip().split()]

tom_sum = tom[0] + tom[1]
jerry_sum = jerry[0] + jerry[1]

if tom_sum > jerry_sum:
    print('Tom')
elif jerry_sum > tom_sum:
    print('Jerry')
else:
    if tom[0] == tom[1] and jerry[0] != jerry[1]:
        print('Tom')
    elif jerry[0] == jerry[1] and tom[0] != tom[1]:
        print('Jerry')
    else:
        print('It is a Tie!')

# if tom[0] == tom[1] and jerry[0] != jerry[1] or tom_sum > jerry_sum:
#     print('Tom')
# elif jerry[0] == jerry[1] and tom[0] != tom[1] or jerry_sum > tom_sum:
#     print('Jerry')
# else:
#     print('It is a Tie!')

# if tom_sum > jerry_sum:
#     print('Tom')
# elif tom_sum < jerry_sum:
#     print('Jerry')
# else:
#     if tom[0] == tom[1] and jerry[0] != jerry[1]:
#         print('Tom')
#     else:
#
#     print("It's a tie")

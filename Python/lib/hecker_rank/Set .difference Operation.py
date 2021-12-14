number_of_english_subscribe = int(input())
english_subscribed_rolls = [int(inp_eng) for inp_eng in input().split()]
number_of_french_subscribe = int(input())
french_subscribed_rolls = [int(inp_fre) for inp_fre in input().split()]
difference = []

for x in english_subscribed_rolls:
    if x not in french_subscribed_rolls:
        difference.append(x)


print(len(difference))

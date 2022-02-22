from collections.abc import Iterable

a = 1
print(type(a))
if isinstance(a, int):
    print('a is a ')

# invoice = {
#     "id": 1,
#     "date": "2022-02-22",
#     "ok": [1, 2],
#     "items": {
#         "item": "Pen",
#         "quantity": 10,
#         "unitprice": 25.5
#     },
#     "total": 255.0
# }
invoice = [
    1,
    2,
    3,
    [
        4,
        5,
        6
    ],
    {
        1: 2
    }
]
# if isinstance(invoice, Iterable)
'''
Output:
1
2022-02-22
Pen
10
25.5
255.0
'''
for i in invoice:
    if isinstance(invoice[i], list) or isinstance(invoice[i], tuple) or isinstance(invoice[i], dict):
        for x in invoice[i]:
            print(invoice[i][x])
    else:
        print(invoice[i])

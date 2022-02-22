# invoice = [
#     1,
#     {
#         "id": 2,
#         "epic iq": 2000,
#         "ok": [2, 3]
#     }
# ]
invoice = [1, 2, [3, 4, [5, 6, [7, 8, 9, [10, 11, 12]]]]]
l = invoice
# if isinstance(invoice, dict):
#     for i in invoice:
#         z = invoice[i]
#         if isinstance(z, int) or isinstance(z, float) or isinstance(z, bool) or isinstance(z, str):
#             print(z)
#         else:
#             if isinstance(z, list):
#                 for y in z:
#                     print(y)
#             elif isinstance(z, tuple):
#                 for y in z:
#                     print(y)
#             elif isinstance(z, set):
#                 for y in z:
#                     print(y)
#             elif isinstance(z, dict):
#                 for y in z:
#                     print(z[y])
# elif isinstance(invoice, list):
x = 0
while True:
    for i in invoice:
        if isinstance(i, int) or isinstance(i, float) or isinstance(i, bool) or isinstance(i, str):
            print(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            invoice = i
        elif isinstance(i, dict):
            invoice = i
    if l[-1] == invoice:
        break

# elif isinstance(i, dict):
# if isinstance(x, int) or isinstance(x, float) or isinstance(x, bool) or isinstance(x, str):
# if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):

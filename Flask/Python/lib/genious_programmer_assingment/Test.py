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

# if isinstance(invoice, Iterable)
def is_iterator(i):
    if isinstance(i, list) \
            or isinstance(i, tuple) \
            or isinstance(i, set):
        return 1
    elif isinstance(i, dict):
        return 2
    else:
        return 0


def extract(some_object):
    if is_iterator(some_object) == 1:
        for x in some_object:
            extract(x)
    elif is_iterator(some_object) == 2:
        for x in some_object.values():
            extract(x)
    else:
        print(some_object)


# object = [1, 2, [4, 5, 6], [1, 2, [12, 13, [23, 43, {"k": "v"}]]]]
extract({'Tahsin': [1, 2], 'Ayman': 3})

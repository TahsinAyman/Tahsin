def extract(obj):
    if isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set):
        for i in obj:
            extract(i)
    elif isinstance(obj, dict):
        for i in obj.values():
            extract(i)
    else:
        print(obj)


if __name__ == '__main__':
    var = [{
        'items': 12,
        'something': {
            'its nothing': [123, [132, [[[10]]]]]
        }
    }]
    extract(var)  # Input Values Here


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
    extract([])  # Input Values Here


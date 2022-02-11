with open('file.txt', 'r') as file:
    lst = file.read().replace('\n', ' ').split()
    try:
        lst.remove()
    except Exception:
        pass
print(lst)

# apple banana cherry apple cherry
'''
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley

'''
lst = []
cnt = 0
while True:
    txt = input().split()
    for arr in txt:
        lst.append(arr)
    if len(txt) <= 0:
        break


print(lst)
search = input('Enter the Value to Search: ')
for word in lst:
    if search.upper() == word.upper():
        cnt += 1
print(cnt)

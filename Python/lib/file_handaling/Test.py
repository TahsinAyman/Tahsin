with open('shakespeare-hamlet.txt', 'r') as file:
    y, times, main = [], [], file.read().replace('\n', ' ').lower()
    for v in range(int(input())):
        y.append(input().lower())
    for _ in ['!', '@', '#', '$', '%', '^', '&''*', '(', ')', '-', '', '+', '+', '{', '}', '[', ']', ':', ':', "'", '"',
              ',', '/', '?', '.', '`']:
        main = main.replace(_, ' ')
    main.split()
    for o in y:
        print(main.count(o))

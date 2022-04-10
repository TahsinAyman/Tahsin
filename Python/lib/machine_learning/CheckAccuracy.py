def accuracy(x, y, t_s):
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score

    if t_s < 100:
        s = str(t_s)
        s = "0." + s
        t_s = float(s)
    elif t_s == 100:
        t_s = 1

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=t_s)
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    predcitons = model.predict(x_test)

    score = accuracy_score(y_test, predcitons)
    if score == 1.0:
        return 100
    else:
        s = str(score)
        index = None

        for i in range(len(s)):
            if s[i] == '.':
                index = i
        s = s[index+1:]
        score = int(s[:2])
        return score

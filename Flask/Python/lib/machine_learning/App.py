import pandas
from sklearn.tree import DecisionTreeClassifier
import joblib
from CheckAccuracy import accuracy


model = joblib.load('trained_machine.joblib')
predictions = list(model.predict([[21, 1], [21, 0]]))
print(predictions)

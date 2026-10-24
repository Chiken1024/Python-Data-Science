import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


data: pd.DataFrame = pd.read_csv("titanic.csv")

data["Age"] = data["Age"].fillna(data["Age"].median())
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])


encoder: LabelEncoder = LabelEncoder()

features: pd.DataFrame = data.drop(
  columns=["Survived", "PassengerId", "Ticket", "Name", "Cabin"]
)
for i in features.select_dtypes(include=str):
  features[i] = encoder.fit_transform(features[i])

target: pd.Series = data["Survived"]


x_train, x_test, y_train, y_test = train_test_split(features, target)

tree: DecisionTreeClassifier = DecisionTreeClassifier(max_depth=3)
tree.fit(x_train, y_train)

y_pred = tree.predict(x_test)

print(
  accuracy_score(y_test, y_pred),
  classification_report(y_test, y_pred),
  confusion_matrix(y_test, y_pred)
)
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

iris: pd.DataFrame = pd.read_csv("iris.csv")

encoder: LabelEncoder = LabelEncoder()

iris["species"] = encoder.fit_transform(iris["species"])

features: pd.DataFrame = iris.drop(columns=["species"])
target: pd.Series = iris["species"]

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

tree: DecisionTreeClassifier = DecisionTreeClassifier(max_depth=3)

tree.fit(x_train, y_train)

y_pred = tree.predict(x_test)

print(
  accuracy_score(y_test, y_pred),
  classification_report(y_test, y_pred),
  confusion_matrix(y_test, y_pred)
)
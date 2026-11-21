import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


data: pd.DataFrame = pd.read_csv("adult_income.csv", header=None)

data.columns = [
  "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
  "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
  "hours-per-week", "native-country", "income"
]

encoder: LabelEncoder = LabelEncoder()

for column in data.select_dtypes("str"):
  data[column] = encoder.fit_transform(data[column])


features: pd.DataFrame = data.drop(columns=["income"])
target: pd.DataFrame = data["income"]

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

tree = DecisionTreeClassifier(max_depth=3)

tree.fit(x_train, y_train)

y_pred = tree.predict(x_test)

print(
  f"{accuracy_score(y_test, y_pred) * 100:.2f}%",
  classification_report(y_test, y_pred),
  confusion_matrix(y_test, y_pred)
)


"""
Predict persons income bracket by tree model
https://archive.ics.uci.edu/dataset/2/adult
"""
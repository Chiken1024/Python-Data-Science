import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import seaborn
import matplotlib.pyplot as plt


car_data: pd.DataFrame = pd.read_csv("car_evaluation.csv")

car_data.columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "condition"]


print(car_data["condition"].value_counts())


encoder: LabelEncoder = LabelEncoder()

for column in car_data.select_dtypes("str"):
  car_data[column] = encoder.fit_transform(car_data[column])


print(car_data["condition"].value_counts())


features: pd.DataFrame = car_data.drop(columns=["condition"])
target: pd.Series = car_data["condition"]

# print(features.shape, target.shape)

# smote: SMOTE = SMOTE(random_state=42)
# features, target = smote.fit_resample(features, target)

# print(features.shape, target.shape)

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

tree = DecisionTreeClassifier(max_depth=3)

tree.fit(x_train, y_train)

y_pred = tree.predict(x_test)


print(
  f"{accuracy_score(y_test, y_pred) * 100:.2f}%",
  classification_report(y_test, y_pred),
  confusion_matrix(y_test, y_pred)
)




mat = confusion_matrix(y_test, y_pred)

seaborn.heatmap(mat, annot=True, xticklabels=["acc", "good", "unacc", "vgood"], yticklabels=["acc", "good", "unacc", "vgood"])

plt.show()
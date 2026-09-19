import pandas as pd

dataframe: pd.DataFrame = pd.read_csv("titanic.csv")

# group = dataframe.groupby("Sex")

# print(group["Age"].mean(), group["Fare"].mean())

# group = dataframe.groupby(["Sex", "Pclass"])

# print(group["Fare"].mean())

# group = dataframe[dataframe["Survived"]==1].groupby("Pclass")

# print(group["Survived"].count())

group = dataframe.groupby(["Pclass", "Sex"])

print(group["Age"].max())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe: pd.DataFrame = pd.read_csv("titanic.csv")

groups = dataframe.groupby("Sex")

#print(groups.get_group((1, 1)))

# print(dataframe[["Age", "Fare"]].median())

# print(dataframe.agg({"Age": ["mean", "min", "max"], "Fare": ["mean"]}))

# print(groups["Age"].mean())

print(dataframe["Name"].str[::2])

plt.scatter([1, 2, 3, 4, 5], [0.5, 1.0, 1.5, 2.0, 2.5])
plt.show()
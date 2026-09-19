import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

dataframe: pd.DataFrame = pd.read_csv("titanic.csv")

groups = dataframe.groupby("Sex")

#print(groups.get_group((1, 1)))

# print(dataframe[["Age", "Fare"]].median())

# print(dataframe.agg({"Age": ["mean", "min", "max"], "Fare": ["mean"]}))

# print(groups["Age"].mean())

print(dataframe["Name"].str[::2])

x = np.arange(-10, 10, 0.5)
y = np.sin(x)
plt.plot(x, y)
plt.show()
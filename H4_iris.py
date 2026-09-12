import pandas as pd

iris: pd.DataFrame = pd.read_csv("iris.csv")

mean_min_max: pd.DataFrame = pd.DataFrame(
  [
    [
      measurement,
      iris[measurement].mean(),
      iris[measurement].min(),
      iris[measurement].max()
    ]
    for measurement in iris.columns[:-1]
  ],
  columns=["measurement", "avg", "min", "max"]
)

print(mean_min_max)

print(iris["species"].value_counts())
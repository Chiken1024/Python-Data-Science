import pandas as pd

customers: pd.DataFrame = pd.read_csv("Mall_Customers.csv")

customers = customers.drop(columns=["CustomerID"])

customers.rename(columns={"Gender": "Sex"}, inplace=True)

customers["Sex"] = customers["Sex"].replace({"Male": 0, "Female": 1})
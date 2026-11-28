import pandas as pd
import matplotlib.pyplot as plt


data: pd.DataFrame = pd.read_csv("Uber_Pickups.csv")

data["date"] = pd.to_datetime(data["date"])


print(data["date"][0].year)


# day_counts = data.groupby(data["date"])

# print(day_counts["trips"].sum().sort_values(ascending=False))


# plt.plot(data["date"].unique(), day_counts["trips"].sum())

# plt.show()
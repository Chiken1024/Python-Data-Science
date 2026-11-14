import pandas as pd
import matplotlib.pyplot as plt

data: pd.DataFrame = pd.read_csv("covid_data_over_time.csv")

data["DateReported"] = pd.to_datetime(data["DateReported"])

data = data[data["Country"]=="United States of America"]

data_2020 = data[data["DateReported"].dt.year==2020]
data_2021 = data[data["DateReported"].dt.year==2021]

figure = plt.figure(figsize=(15, 5))
plt.scatter(data_2020["DateReported"], data_2020["Cumulative_cases"], c="r")
plt.scatter(data_2021["DateReported"], data_2021["Cumulative_cases"], c="b")

plt.show()
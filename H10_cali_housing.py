import pandas as pd
import matplotlib.pyplot as plt


housing: pd.DataFrame = pd.read_csv("housing.csv")

housing = housing[housing["median_house_value"]<500_000]


figure, axes = plt.subplots(2, 2, figsize=[10, 10])

axes[0, 0].set_title("Median house value vs median income")
axes[0, 0].scatter(housing["median_house_value"], housing["median_income"])
axes[0, 0].set_xlabel("Median house value")
axes[0, 0].set_ylabel("Median income")

axes[1, 0].set_title("Housing median age")
axes[1, 0].hist(housing["housing_median_age"], [i*5 for i in range(12)])
axes[1, 0].set_xlabel("Median age")

axes[0, 1].set_title("Median house value based on location")
axes[0, 1].scatter(housing["latitude"], housing["longitude"], c=housing["median_house_value"])
axes[0, 1].set_xlabel("Latitude")
axes[0, 1].set_ylabel("Longitude")

plt.show()
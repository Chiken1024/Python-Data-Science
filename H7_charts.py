import pandas as pd
import matplotlib.pyplot as plt

dataset: pd.DataFrame = pd.read_csv("titanic.csv")

figure, axes = plt.subplots(2, 2, figsize=[10, 10])

axes[0, 0].set_title("Number of men and women")
axes[0, 0].bar(dataset["Sex"].value_counts().index, dataset["Sex"].value_counts())

gender = dataset.groupby(["Sex"])
axes[0, 1].set_title("Average fare of men and women")
axes[0, 1].bar(gender["Fare"].mean().index, gender["Fare"].mean())

axes[1, 0].set_title("People of different classes")
orig_pos = axes[1, 0].get_position()
axes[1, 0].pie(dataset["Pclass"].value_counts())
axes[1, 0].set_position([orig_pos.x0 + 0.15, orig_pos.y0 - 0.1, orig_pos.x1, orig_pos.y1])

axes[1, 1].axis("off")

plt.show()
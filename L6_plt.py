import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# x = np.arange(-10, 10, 0.5)
# y = np.arange(-20, 20, 1)

# plt.figure(figsize=(5, 5))
# plt.plot(x, np.sin(x), "r-", linewidth=5, label="red")
# plt.plot(x, np.cos(x), "b-", linewidth=5, label="blue")

# plt.axis((-10, 10, -20, 25))
# #plt.xticks(np.arange(-10, 10, 0.5))
# #plt.xlim(-5, 5)

# plt.title("graph")
# plt.xlabel("time (s)")
# plt.ylabel("position (m)")
# plt.legend()

# plt.show()

dataframe: pd.DataFrame = pd.read_csv("titanic.csv")

plt.figure(figsize=(5, 5))

genders = dataframe.groupby(["Sex", "Survived"])

counts = genders.size().unstack()

plt.bar(
  [1, 4],
  counts[0],
  width=1,
  label="Passed"
)

plt.bar(
  [2, 5],
  counts[1],
  width=1,
  label="Survived"
)

plt.xticks([1.5, 4.5], ["female", "male"])
plt.ylabel("People")
plt.legend()

plt.show()
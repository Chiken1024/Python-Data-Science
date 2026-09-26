import matplotlib.pyplot as plt

ages: list[int] = [27, 45, 20, 36, 19, 31, 49, 23, 36, 29, 20, 41, 32]

plt.figure(figsize=(10, 7))

# plt.hist(ages, bins=10, edgecolor="black")

lst: list[int] = [1, 5, 2, 3]

plt.pie(lst, labels=["1", "2", "3", "4"], colors=["r", "g", "b", "m"], autopct="%.2f%%", explode=[0.1, 0, 0, 0], shadow=True)

plt.show()
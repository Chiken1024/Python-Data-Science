import matplotlib.pyplot as plt
from random import randint

marks: list[int] = [randint(0, 100) for _ in range(50)]

plt.xticks([15, 40, 60, 80, 95], ["0-30", "31-50", "51-70", "71-90", "91-100"])
plt.xlabel("Grade")

plt.hist(marks, [0, 30, 50, 70, 90, 100], edgecolor="#000")
plt.show()
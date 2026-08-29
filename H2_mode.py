import numpy as np

def get_mode(arr: np.ndarray) -> tuple[int, int]:
  items: dict[int, int] = {}

  for item in arr:
    if item in items.keys(): items[item] += 1
    else: items.update({item: 1})

  mode: tuple[int, int] = (0, 0)

  for count in items.items():
    if count[1] > mode[1]: mode = count

  return mode

print(get_mode(np.array([1, 2, 7, 4, 5, 2, 2, 4, 9])))
import numpy as np

lst: list[int] = [1, 2, 3]
arr: np.ndarray = np.array(lst)

print(type(arr))
print(arr.shape)
print(arr.ndim)
print(arr.size)

arr2: np.ndarray = np.arange(0, 84)

print(len(arr2))

arr3 = np.linspace(0, 1, 4)

print(arr3)

lst_2d: list[list] = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
arr_2d: np.ndarray = np.array(lst_2d)

print(arr_2d, arr_2d.shape, arr_2d.size, len(arr_2d))

arr2_reshape: np.ndarray = arr2.reshape(7, 3, 4)
print(arr2_reshape, "\n", arr2_reshape.shape)

print(np.random.randint(0, 10, (2, 4, 5)))

""" Generate a list of numbers from 1 - 100000 and time it. Find out the difference between list and numpy, and check which is faster. """
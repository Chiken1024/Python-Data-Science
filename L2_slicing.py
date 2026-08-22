import numpy as np
import scipy as sp

arr: np.ndarray = np.array([i for i in range(10, 30)])

lst: list = [i for i in range(0, 10)]
lst_add_10: list = [num + 10 for num in lst]
print(lst_add_10)

arr_2d: np.ndarray = np.array([[j + i * 10 for j in range(10)] for i in range(10)])
print(arr_2d[0:5,0:5])

mat1: np.matrix = np.matrix([[2, 3], [4, 5]])
mat2: np.matrix = np.matrix([[4, 5], [0, 2]])

print(np.matmul(mat1, mat2))

y = np.arange(0 + 3, 10 + 3, 2)
print(y)

def y(x: int | np.ndarray) -> int | np.ndarray:
  return 2 * x + 3

print(y(arr), sp.stats.mode(y(arr)))

""" Create a user defined function to get the mode of a numpy ndarray. """
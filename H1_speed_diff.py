""" Speed test """
import time

TEST_RANGE: tuple[int] = (1, 100000)

# List
t1: float = time.time()
lst: list[int] = [n for n in range(*TEST_RANGE)]
t2: float = time.time()

dt_list: float = t2 - t1

# Numpy array
import numpy

t1 = time.time()
arr: numpy.ndarray[int] = numpy.arange(*TEST_RANGE)
t2 = time.time()

dt_array: float = t2 - t1

# Evaluation
winner: str = "List" if dt_list < dt_array else "Array"

diff_abs: float = abs(dt_list - dt_array) * 1000

diff_rel: float = dt_array / dt_list if winner == "List" else dt_list / dt_array

print(f"""
List:  {dt_list * 1000: .2f}ms
Array: {dt_array * 1000: .2f}ms

{winner} was done{diff_rel: .2f}x faster, saving{diff_abs: .2f}ms
""")
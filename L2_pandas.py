import pandas as pd

lst: list = [0, "abc", 10.0, True]
series: pd.Series = pd.Series(lst)

series_2: pd.Series = pd.Series([1, 6, 3, 100, 75, 43, 86, 3, 100])
print(series_2.mode())
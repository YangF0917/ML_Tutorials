import pandas as pd
import numpy as np

# 1d Data
series = pd.Series(5)
# Newline to separate series print statements
print('{}\n'.format(series))

series = pd.Series(5)
print('{}\n'.format(series))

series = pd.Series([1, 2, 3])
print('{}\n'.format(series))

series = pd.Series([1, 2.2]) # upcasting
print('{}\n'.format(series))

arr = np.array([1, 2])
series = pd.Series(arr, dtype=np.float32)
print('{}\n'.format(series))

series = pd.Series([[1, 2], [3, 4]])
print('{}\n'.format(series))

# Indexing
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print('{}\n'.format(series))

series = pd.Series([1, 2, 3], index=['a', 8, 0.3])
print('{}\n'.format(series))
# Turns the information into a "dict" like structure

# Dictionary Input:
series = pd.Series({'a':1, 'b':2, 'c':3})
print('{}\n'.format(series))

series = pd.Series({'b':2, 'a':1, 'c':3})
print('{}\n'.format(series))
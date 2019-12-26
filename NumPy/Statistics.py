import numpy as np

# Analysis
arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
print(arr.min())
print(arr.max())

print(repr(arr.min(axis=0)))
print(repr(arr.max(axis=-1)))
# Notice that the outliers can be found in this way

# Statistical Methods
arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
print(np.mean(arr))
print(np.var(arr))
print(np.median(arr))
print(repr(np.median(arr, axis=-1)))
# Notice that the variance is high due to the outliers in the data set
# https://docs.scipy.org/doc/numpy/reference/routines.statistics.html for more stat methods



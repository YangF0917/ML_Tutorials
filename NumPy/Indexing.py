import numpy as np

# Array Accessing
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[4])

arr = np.array([[6, 3], [0, 2]])
# Subarray
print(repr(arr[0]))
# Accessing an element in an 1d array is identical to most other langs

# Sub-arrays
arr = np.array([1, 2, 3, 4, 5])
print(repr(arr[:]))
print(repr(arr[1:]))
print(repr(arr[2:4]))

# Cuts 1 element from the end
print(repr(arr[:-1]))
# Takes only the last 2 elements
print(repr(arr[-2:]))

# 2D array Splicing
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(repr(arr[:]))
print(repr(arr[1:]))
print(repr(arr[:, -1]))
print(repr(arr[:, 1:]))
print(repr(arr[0:1, 1:]))
print(repr(arr[0, 1:]))
# Note that the comma indicates how to splice each dimension respectively


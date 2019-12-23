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

# Argmin and Argmax
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])
print(np.argmin(arr[0]))
print(np.argmax(arr[2]))
print(np.argmin(arr))
# Returns the index of the largest/smallest element in the array
# Using this operation on an multi-dimension array will return the index based on the flattened array

arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])
print(repr(np.argmin(arr, axis=0)))
# returns the max row for each column
print(repr(np.argmin(arr, axis=1)))
# retuns max column for each row
print(repr(np.argmax(arr, axis=-1)))


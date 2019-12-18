import numpy as np

# Arrays
arr = np.array([[0, 1, 2], [3, 4, 5]],
               dtype=np.float32)
print(repr(arr))

arr = np.array([0, 0.1, 2])
# Data types are "rounded up", so the integers are automatically casted to floats
print(repr(arr))

# Copying
a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 5
print('Array a: {}'.format(repr(a)))

# Setting c = a will make c the same instance as a
d = b.copy()
d[0] = 6

# We can create a copy of the instance using the .copy() function
print('Array b: {}'.format(repr(b)))

# Casting
arr = np.array([0, 1, 2])
print(arr.dtype)
arr = arr.astype(np.float32)
print(arr.dtype)

# The astype function will cast all elements in the array to the specified data type

# NaN
arr = np.array([np.nan, 1, 2])
print(repr(arr))

arr = np.array([np.nan, 'abc'])
print(repr(arr))

# Will result in a ValueError
# np.array([np.nan, 1, 2], dtype=np.int32)
# NaN is used as a placeholder for data

# Infinity
print(np.inf > 1000000)

# Infinity represented by np.inf
arr = np.array([np.inf, 5])
print(repr(arr))

# -Inf represented by -np.inf
arr = np.array([-np.inf, 1])
print(repr(arr))

# Will result in an OverflowError
# np.array([np.inf, 3], dtype=np.int32)

# Exercise
arr = np.array([np.nan, 2, 3, 4, 5])
arr2 = np.copy(arr)
arr2[0] = 10
float_arr = np.array([1, 5.4, 3])
float_arr2 = arr2.astype(np.float32)
float_arr2 = np.array([1,2,3],dtype=np.float32)
matrix = np.array([[1,2,3],[4,5,6]],dtype=np.float32)
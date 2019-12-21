import numpy as np

# Ranged data
arr = np.arange(5)
# If only 1 argument is given [0,n)
print(repr(arr))

arr = np.arange(5.1)
print(repr(arr))

arr = np.arange(-1, 4)
# 2 arguments given [m,n)
print(repr(arr))

arr = np.arange(-1.5, 4, 2)
print(repr(arr))

# np.arange(s, f, step)
# s is the first value in the list
# f is the upper bound of output
# step is how much to increment > decrement to get the next element

arr = np.linspace(5, 11, num=4)
print(repr(arr))
# Creates a list of 4 equally spaced numbers from 5 to 11 inclusive

arr = np.linspace(5, 11, num=4, endpoint=False)
print(repr(arr))
# Creates a list of 5 equally spaced numbers excluding the last one

arr = np.linspace(5, 11, num=4, dtype=np.int32)
print(repr(arr))
# Same as the first one, except casts the values to integers

# Reshape Function
arr = np.arange(8)

reshaped_arr = np.reshape(arr, (2, 4))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))
# Places the elements in the array into a 2d array size [2][4]

reshaped_arr = np.reshape(arr, (-1, 2, 2))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))
# -1 puts the required dimension to fit all the elements into the new array

# Flattening arrays
arr = np.arange(8)
arr = np.reshape(arr, (2, 4))
flattened = arr.flatten()
print(repr(arr))
print('arr shape: {}'.format(arr.shape))
print(repr(flattened))
print('flattened shape: {}'.format(flattened.shape))
# Basically the opposite of reshape, turns into a 1d array

# Transposing an array
arr = np.arange(8)
arr = np.reshape(arr, (4, 2))
transposed = np.transpose(arr)
print(repr(arr))
print('arr shape: {}'.format(arr.shape))
print(repr(transposed))
print('transposed shape: {}'.format(transposed.shape))
# Takes a 2d array and flips its dimensions. Ex.  [2][4] -> [4][2]

arr = np.arange(24)
arr = np.reshape(arr, (3, 4, 2))
transposed = np.transpose(arr, axes=(1, 2, 0))
print('arr shape: {}'.format(arr.shape))
print('transposed shape: {}'.format(transposed.shape))
# np.transpose can also take in the order to transpose the array
# Default transposing is a reflection

# Generating arrays with zeros and ones
arr = np.zeros(4)
print(repr(arr))
# [0., 0., 0., 0.]

arr = np.ones((2, 3))
print(repr(arr))
# [1., 1., 1.]
# [1., 1., 1.]

arr = np.ones((2, 3), dtype=np.int32)
print(repr(arr))
# [1, 1, 1]
# [1, 1, 1]

# Creating arrays of ones and zeros of the same format as another array
arr = np.array([[1, 2], [3, 4]])
print(repr(np.zeros_like(arr)))

arr = np.array([[0., 1.], [1.2, 4.]])
print(repr(np.ones_like(arr)))
print(repr(np.ones_like(arr, dtype=np.int32)))

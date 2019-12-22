import numpy as np

# Psuedo-random Integer Generation
print(np.random.randint(5))
print(np.random.randint(5))
print(np.random.randint(5, high=6))
# [5,6)
random_arr = np.random.randint(-3, high=14,
                               size=(2, 2))
# [-3, 14) in a [2][2] matrix
print(repr(random_arr))

# Utility Functions
np.random.seed(1)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100,
                               size=(2, 2))
print(repr(random_arr))

# New seed
np.random.seed(2)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100,
                               size=(2, 2))
print(repr(random_arr))

# Original seed
np.random.seed(1)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100,
                               size=(2, 2))
print(repr(random_arr))
# Seeds store the states of random numbers generated

# Shuffling Arrays
vec = np.array([1, 2, 3, 4, 5])
np.random.shuffle(vec)
print(repr(vec))
np.random.shuffle(vec)
print(repr(vec))

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
np.random.shuffle(matrix)
print(repr(matrix))
# Note, this will shuffle only the first dimension
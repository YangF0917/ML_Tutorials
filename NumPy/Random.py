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
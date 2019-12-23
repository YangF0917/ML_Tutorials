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

# Distributions
print(np.random.uniform())
print(np.random.uniform(low=-1.5, high=2.2))
print(repr(np.random.uniform(size=3)))
print(repr(np.random.uniform(low=-3.4, high=5.9,
                             size=(2, 2))))
# Generates numbers based on an uniform distribution

print(np.random.normal())
print(np.random.normal(loc=1.5, scale=3.5))
print(repr(np.random.normal(loc=-2.4, scale=4.0,
                            size=(2, 2))))
# loc represents the mean, scale represents std deviation
# Random numbers taken using normal distribution

# Random choice
colors = ['red', 'blue', 'green']
print(np.random.choice(colors))
print(repr(np.random.choice(colors, size=2)))
print(repr(np.random.choice(colors, size=(2, 2),
                            p=[0.8, 0.19, 0.01])))
# p gives the probability of each event occuring (must sum to 1)

# Useful for generating random data based on probabilities given or by distribution
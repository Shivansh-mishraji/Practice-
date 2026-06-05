# Practice script for basic Numpy operations like mean, variance, and reshape
# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Return mean
print("Mean:", np.mean(matrix))
# Output: 5.0

# Return variance
print("Variance:", np.var(matrix))
# Output: 6.666666666666667

# Return standard deviation
print("Std Dev:", np.std(matrix))
# Output: 2.581988897471611

# Find the mean value in each column
print("Mean (axis=0):", np.mean(matrix, axis=0))
# Output: array([ 4.,  5.,  6.])

# Create 4x3 matrix
matrix2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])

# Reshape matrix into 2x6 matrix
print("Reshaped:\n", matrix2.reshape(2, 6))
# Output: array([[ 1,  2,  3,  4,  5,  6], [ 7,  8,  9, 10, 11, 12]])

# Create matrix
matrix3 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Transpose matrix
print("Transpose:\n", matrix3.T)
# Output: array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

# Flatten matrix
print("Flattened:", matrix3.flatten())
# Output: array([1, 2, 3, 4, 5, 6, 7, 8, 9])
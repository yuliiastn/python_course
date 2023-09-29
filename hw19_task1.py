import numpy as np

# 1a: Create arrays
# a. all zeros with shape (4, 3)
zeros_array = np.zeros((4, 3))

# b. ones with shape (4, 3)
ones_array = np.ones((4, 3))

# c. numbers from 0 to 11
numbers_array = np.arange(12).reshape(4, 3)

# 1b: Tabulate F(x) = 2x^2 + 5 for x in [1, 100] with step 1
x_values = np.arange(1, 101)
result_b = 2 * x_values**2 + 5

# 1c: Tabulate F(x) = e^(-x) for x in [-10, 10] with step 1
x_values = np.arange(-10, 11)
result_c = np.exp(-x_values)

print("a. Array of all zeros:")
print(zeros_array)

print("\nb. Array of ones:")
print(ones_array)

print("\nc. Array of numbers from 0 to 11:")
print(numbers_array)

print("\nb. Tabulated F(x) = 2x^2 + 5 for x in [1, 100]:")
print(result_b)

print("\nc. Tabulated F(x) = e^(-x) for x in [-10, 10]:")
print(result_c)

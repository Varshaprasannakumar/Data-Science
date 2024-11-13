import numpy as np
X = np.array([[1, 2,3 ],
[4, 5, 6],
[7, 8, 9]])

X_cube_multiply = np.multiply(X, np.multiply(X, X))
X_cube_operator = X * X * X
X_cube_power = np.power(X, 3)
X_cube_double_star = X ** 3
identity_matrix = np.identity(X.shape[0])
X_power_2 = np.power(X, 2)
X_power_3 = np.power(X, 3)
X_power_4 = np.power(X, 4)
print("Original Matrix X:\n", X)
print("\nCubed Matrix (Method 1 - multiply()):\n", X_cube_multiply)
print("\nCubed Matrix (Method 2 - * operator):\n", X_cube_operator)
print("\nCubed Matrix (Method 3 - power()):\n", X_cube_power)
print("\nCubed Matrix (Method 4 - ** operator):\n", X_cube_double_star)
print("\nIdentity Matrix:\n", identity_matrix)
print("\n\nMatrix to Different Powers:\n")
print("X^2:\n", X_power_2)
print("\nX^3:\n", X_power_3)
print("\nX^4:\n", X_power_4)

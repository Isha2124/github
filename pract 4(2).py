import numpy as np

print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input().split()))
    B.append(row)

# Convert to numpy arrays
A = np.array(A)
B = np.array(B)

# Multiply matrices
C = np.dot(A, B)

# Output
print("Product Matrix (5x2):\n", C)
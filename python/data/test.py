import numpy as np

A = np.linspace(0, 2, 5)
print(A)
print(np.diff(A) ** 2)
B = np.diff(A)*2
print(B)
print(B == np.ones(4))

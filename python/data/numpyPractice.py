import numpy as np


a = np.array([1,2,3])
print(a)
print(type(a))
print(a.shape)

b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)

c1 = np.arange(6)
print(c1)

c2 = c1.reshape((2,3))
print(c2)

c3 = c2.ravel()
print(c3)

c4 = c2.flatten()
print(c4)
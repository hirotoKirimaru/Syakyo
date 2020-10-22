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

print(a.dtype)

d = np.array([1,2], dtype=np.int16)
print(d.dtype)

print(d.astype(np.float16))
print(d)

# インデックスとスライス
print("*********************************")

print(a)
print(a[0])
print(a[1:])
print(a[-1])

print(b)
print(b[0])
print(b[1, 0])
print(b[:, 2])
print(b[1, :])
print(b[0, 1:])
print(b[:, [0,2]])


# でーたさいとうにゅう
print("*********************************")





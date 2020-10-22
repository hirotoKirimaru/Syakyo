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

print(a)
a[2] = 4

print(a)
print(b)

b[1, 2] = 7
print(b)

b[:,2] = 8
print(b)

# 深いコピー(copy)
print("*********************************")
a1 = a
print(a1)

a1[1] = 5
print(a1)
print(a)

a2 = a.copy()
print(a2)
a2[0] = 6
print(a2)
print(a)

# pythonとnumpyでスライスした結果は異なる
print("*********************************")
py_list1= [0,1]
py_list2 = py_list1[:]
py_list2[0] = 2
print(py_list1)
print(py_list2)

np_array1 = np.array([0, 1])
np_array2 = np_array1[:]
np_array2[0] = 2
print(np_array1)
print(np_array2)



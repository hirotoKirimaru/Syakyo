import numpy as np


a = np.array([1, 2, 3])
print(a)
print(type(a))
print(a.shape)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)

c1 = np.arange(6)
print(c1)

c2 = c1.reshape((2, 3))
print(c2)

c3 = c2.ravel()
print(c3)

c4 = c2.flatten()
print(c4)

print(a.dtype)

d = np.array([1, 2], dtype=np.int16)
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
print(b[:, [0, 2]])


# でーたさいとうにゅう
print("*********************************")

print(a)
a[2] = 4

print(a)
print(b)

b[1, 2] = 7
print(b)

b[:, 2] = 8
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
py_list1 = [0, 1]
py_list2 = py_list1[:]
py_list2[0] = 2
print(py_list1)
print(py_list2)

np_array1 = np.array([0, 1])
np_array2 = np_array1[:]
np_array2[0] = 2
print(np_array1)
print(np_array2)

# 数列を返す
print("*********************************")
print(np.arange(10))
print(np.arange(1, 11))
print(np.arange(1, 11, 2))

f = np.random.random((3, 2))
print(f)

np.random.seed(123)
print(np.random.random((3, 2)))

np.random.seed(123)
print(np.random.rand(4,2))

print(np.random.randint(1, 10))
print(np.random.randint(1, 10, (3,3)))
print(np.random.uniform(0.0, 5.0, size=(2, 3)))

print(np.random.uniform(size=(4,3)))
print(np.random.randn(4,2))


# 同じ要素の数列を作る
print("*********************************")
print(np.zeros(3))
print(np.zeros((2, 3)))

print(np.ones(2))
print(np.ones((3,4)))
print(np.eye(3))

print(np.full(3, 3.14))
print(np.full((2,4), np.pi))

print(np.nan)

print(np.array([1, 2, np.nan]))
print(np.linspace(0, 1, 5))
print(np.linspace(0, np.pi, 21))


# 要素間の差分
print("*********************************")
l = np.array([2, 2,6,1,3])
print(np.diff(l))
print(np.diff(l))

print(a)
print(a1)

print(np.concatenate([a, a1]))

print(b)
b1 = np.array([[10], [20]])
print(b1)

print(np.concatenate([b, b1], axis=1))
print(np.hstack([b, b1]))

b2 = np.array([30, 60, 45])
b3 = np.vstack([b, b2])
print(b3)

# 分割
print("*********************************")

first, second = np.hsplit(b3, [2])
print(first)
print(second)

first1, second1 = np.vsplit(b3, [2])
print(first1)
print(second1)

# 転置
print(b)
print(b.T)

# じげんついか
print(a)
print(a[np.newaxis,:])
print(a[:, np.newaxis])

# グリッドデータの生成
m = np.arange(0,4)
print(m)

n = np.arange(4, 7)
print(n)

xx, yy = np.meshgrid(m, n)
print(xx)
print(yy)


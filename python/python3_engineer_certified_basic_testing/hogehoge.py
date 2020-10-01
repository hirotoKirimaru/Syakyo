v = 1
w = 2
v, w = w + 1, v + 3

print(v, w)
x = w ** 2 + 1
print(x)
y = x - 8 / 2
print(y)
z = y % 5
print(z)
print(w, y, z)

a = [1,3,4,6,3,5]
a.insert(3, -1)
print(a)
a.pop(4)  # popの挙動が0はじまり？
print(a)
a.remove(3)
print(a)
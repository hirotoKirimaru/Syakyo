#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = 10
# x = int(input("Please enter an integer: "))


if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
     print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')



words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))



users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# 既存のコレクションを削除する処理より
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


# 新しいコレクションを作成したほうが通常は理解しやすい
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(users)
print(active_users)


for i in range(5):
    print(i)


array = range(5, 10)
print(array)
array =range(0, 10, 3) 
print(array)

array =range(-10, -100, -30)
print(array)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


print(sum(range(4)))
print(list(range(4)))







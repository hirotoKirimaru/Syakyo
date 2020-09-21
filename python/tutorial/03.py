#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this is the first comment
spam = 1  # and this is the second comment
# ... and now a third!
text = "# This is not a comment because it's inside quotes."


print(text)


print('span eggs')
print('dosen\'t')
print("dosen\'t")
print('"Yes," they said.')
print('\"Yes,\" they said.')
print('"Isn\'t," they said.')

# インタープリタなら\nが改行使いにならない。
s = 'First line.\nSecond line.'
s
print(s)


print("*********************************")


print('C:\some\name')
print(r'C:\some\name')


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


print("*********************************")


print(3 * 'un' + 'ium')
print('Py' 'thon')

print(
    'Put several strings within parentheses '
    'to have them joined together.'

)


prefix = 'Py'
# リテラル同士なら動くけど、変数や式には働きません。
# print(prefix 'thon')


print("*********************************")

word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-6])
print(word[0:2])
print(word[2:5])

print(word[:2] + word[2:])
print(word[:4] + word[4:])

print(word[:2])
print(word[4:])
print(word[-2:])


# out of range
# print(word[42])

print(word[4:42])
print(word[42:])

# 文字列変更はできない
# word[0] = 'J'


print('j' + word[1:])
print(word[:2] + 'py')


print(len(word))

# 3.1.3
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares[:])
print(squares + [36, 49, 64, 81, 100])


cubes = [1, 8, 27, 65, 125]
print(4 ** 3)
cubes[3] = 64
print(cubes)

cubes.append(216)
cubes.append(7**3)
print(cubes)


print('*******')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd']
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print(x[0])
print(x[0][1])

print('3.2')
print('************')

a, b = 0, 1
while a < 10:
    print(a)
    a,b = b, a+b


i = 256*256
print('The value of i is', i)

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

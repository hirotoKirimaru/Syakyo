#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits)
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))

fruits.reverse()

print(fruits)

fruits.append('grape')

print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())



print('*************')


stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)
print(stack.pop())

print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)



print("**********")


squares = []
for x in range(10):
    squares.append(x**2)

print(squares)


squares = list(map(lambda x: x**2, range(10)))

print(squares)
squares = [x**2 for x in range(10)]
print(squares)

# これと
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# これは等価
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)


vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])

print([x for x in vec if x>= 0])

print([abs(x) for x in vec])


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])
# ()つけないとNG
#  [x, x**2 for x in range(6)]


vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

print( [[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)


print(list(zip(*matrix)))

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)
del a[:]
print(a)

t = 12345, 54321, 'hello!'
print(t[0])
print(t)

u = t, (1, 2,3,4,5)
print(u)

# tupple は immutable
# t[0] = 88888


v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))

print(len(singleton))

print(singleton)

x, y, z = t

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket                 )# fast membership testing

print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
print(b)
print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                              # letters in both a and b

print(a ^ b)                              # letters in a or b but not both


a = {x for x in 'abracadabra' if x not in 'abc'}
a
print(a)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))

print(sorted(tel))

print('guido' in tel)

print('jack' not in tel)

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict)
print({x: x**2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)



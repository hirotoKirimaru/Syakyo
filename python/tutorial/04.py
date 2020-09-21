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




print('4.4')

# else句がforにかかっている。
# 素数を求める方法
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
    


# pass文？



def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print() # 改行するだけ
# Now call the function we just defined:
fib(2000)


print(fib)

f = fib
f(100)

fib(0)
print(fib(0))



def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# inputがめんどくさいのでコメントにする
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# デフォルト値は関数を定義している側のスコープで評価される。

i = 5

def f(arg=i):
    print(arg)

i = 6
f()


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))



def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# NGパターン
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


def function(a):
    pass

# function(0, a=0)

# *一個は無名の名前
# **2個はshopkeeper等の名前を付けたやつ
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    #   -----------    ----------     ----------
    #     |             |                  |
    #     |        Positional or keyword   |
    #     |                                - Keyword only
    #      -- Positional only



def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
standard_arg(arg=2)


pos_only_arg(1)
# pos_only_arg(arg=1)

# kwd_only_arg(3)

# combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3)


def foo(name, **kwds):
    return 'name' in kwds

# foo(1, **{'name': 2})

def foo(name, /, **kwds):
    return 'name' in kwds
print(foo(1, **{'name': 2}))
# Trueが返却される？

# 4.7.3.5　要約 ## TODO:チェック！
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)



print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))


print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))
print(f(2))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

def my_function():
     """Do nothing, but document it.

     No, really, it doesn't do anything.
     """
     pass

print(my_function.__doc__)


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))



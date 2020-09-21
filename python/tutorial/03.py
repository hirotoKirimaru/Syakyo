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


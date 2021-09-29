#!/usr/bin/python3

myint1 = 3
myint2 = 5

myfloat1 = 4.2
myfloat2 = 6.5

mystr1 = 'What is your name?'
mystr2 = 'My name is'
mystr3 = 'What is your age?'
mystr4 = 'My age is'
mystr5 = 'Joe Python'
mystr6 = 'What is you grade point average?'
mystr7 = 'My GPA is'

print(mystr1)
print(mystr2 + ' ' + mystr5)

print(myint1)
print(myint1 + myint2)

print(myfloat1)
print(myfloat1 + myfloat2)

print(mystr3)
print(mystr4 + ' ' + repr(myint1))
print('I think my age is' + ' ' + repr(myint1) + ' or maybe it`s ' + repr(myint2))
print(mystr4 + ' ' + 'for sure' + ' ' + repr(myint1 + myint2))

print(mystr6)
print(mystr7 + ' ' + repr(myfloat1))
print('I think my GPA is' + ' ' + repr(myfloat1) + ' or maybe it`s ' + repr(myfloat2))
print(mystr7 + ' ' + 'for sure' + ' ' + repr(myfloat1 + myfloat2))

print('I can also do math, watch this')
print(3 + 2)
print(4.2 * 2)
print(12 / 7)

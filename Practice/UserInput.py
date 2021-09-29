#!/usr/bin/python3

myname = input('What is your name? ')
word = myname

print('Hello ' + myname)

print(myname + ' , Let\'s add two numbers!') #add \ to include the apsotrophy

a = input('Enter the first number: ')
b = input('Enter the second number: ')
c = input('Enter the thrid number: ')
d = input('Enter the fourth number: ')

numbers = a, b, c, d

e = int(a) + int(b)

print('Number entered ' + repr(numbers))

print('The total of ' + a + '+' + b + ' ' + 'is ' + repr(e))

print(word[0]) #indexing retuirn the item

print(word[0:3]) #slicing returns a new word

print(word[3:42]) #handle out of range slice indexes

print('Myc' + word[3:])

print(word[:3] + 'stro')

print(len(myname)) #counts the characters

print(myname.casefold())

if ('Myc' in myname):
    print('Hello Mycstro, Welcome back.')
else:
    print('Hello' + '' + myname + ',' +'' + 'It\'s a pleasure to meet you')

if ('Myc' not in myname):
    print('Hello' + '' + myname + ',' +'' + 'It\'s a pleasure to meet you')
else:
    print('Hello Mycstro, Welcome back.')
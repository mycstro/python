#!/usr/bin/python3

name1 = 'Roaringfir3'
name2 = 'Mycstro'

num1 = 4
num2 = 7

float1 = 4.2
float2 = 7.8

prefix = 'Myc'

text = ('ILLTime Records Forever & ' #to break long strings
		'VSpace coming soon!') #several strings within parentheses 
								#to have them joined together

#Basic Formating

print(text)

print(prefix + 'stro') # concatenate a variable and a literal

print('Roaring' 'fir3') #only works with literals not variables

print(name1 + ' ' + name2)

print(name2 + ' ' + ',' + name1)

print(name1 + ' ' + 'and' + ' ' + name2)

print('g' + (2 * 'o') + 'gle') #concatenated or glued together with + 
								#repeated with *

print("Isn't this cool") #place a statement in double quotes 
							#to include the apostrophy

print('"That\'s what she said", the guy said.') # use this a quote a line

print('Mycstro \nCEO of ILLtime Records') #\n sends the following statement 
											#to the next line

print(r'The Python pratice folder is located at ~/Documents/Python/Pratice') 
			#add an r to use special characters

print("""\
Usage: thingy [options]
		-h			Display this usage message
		-H hostname		Hostname to connect to
""") # prints multiple lines

#sep = seperator
print(name1 , name2, sep='|')
print(name1 , name2, sep=' <--> ')
print(name1, name2, num1, num2, sep=' <--> ')

#Old Format
print('The gamertags are %s and %s' % (name1, name2))
print('The gamerscores are %d and %d' % (num1, num2))

#New Format
print('New: Gamerscore are {} and {}' .format(num1, num2))
print('New: Gamerscores are {0} and {1}' .format(num1, num2))

#Change order
print('New: Gamerscores are {1} and {0}' .format(num1, num2))

#Value conversion


#Align and Padding

#Align left 


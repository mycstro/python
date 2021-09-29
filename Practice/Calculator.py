#!/usr/bin/python3

def option():
    while True:
        print('''
        Please type in the math operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        ** for power
        % for modulo
        mem for last solution
        ac to clear memory
        quit to exit
        ''')
        
        operation = input("Input: ")
                  
        
        if operation == 'quit':
#            quit = 'True'
            break
        
        #Enter a new var
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))
        calculate(operation,  num1,  num2)
         
option()

#Define again() function to ask user if they wish to calculate again
def again(option,  num1,  num2):
    
    #Take input from user
    calc_again = input('''
    Do you wish to quit?
    Please type Y for Yes or N for No.
    ''')
        
    #If user type N
    if calc_again.upper() == 'N':
        calculate(option,  num1,  num2)
        
    #If user type Y
    if calc_again.upper() == 'Y':
        print('Goodbye.')
        
    #If user type another key
    else:
        again(option,  num1,  num2)
            

def calculate(option,  num1,  num2):
    calculation = option
    #Addition
    if calculation == '+':
        x = int(num1 + num2)
        print('{} + {} = {}'.format(num1,  num2,  x))
        
    #Subtraction
    elif calculation == '-':
        x = int(num1 - num2)
        print('{} - {} = {}'.format(num1,  num2,  x))
        
    #Multiplication
    elif calculation == '*':
        x = int(num1 * num2)
        print('{} * {} = {}'.format(num1,  num2,  x))
        
    #Division
    elif calculation == '/':
        x = int(num1 / num2)
        print('{} / {} = {}'.format(num1,  num2,  x))
        
    #Power
    elif calculation == '**':
        x = int(num1 ** num2)
        print('{} ** {} = {}'.format(num1,  num2,  x))
    
    #Modulo
    elif calculation == '%':
        x = int(num1 % num2)
        print('{} % {} = {}'.format(num1,  num2,  x))

        
    #Save last solution
    elif calculation == 'mem':
        print(x)
        
    #Clear memory
    elif calculation == 'ac':
        del(x)
        
    else:
        print("Unknown Input")

again(option,  num1,  num2)

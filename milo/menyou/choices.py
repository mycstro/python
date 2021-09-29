# -*- coding: utf-8 -*-
import sys
import processCommand as pac

def WeHeChoices(p1="default"):
    loop = True

    while loop:  ## While loop which will keep going until loop = False

        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            print("You have selected that you know both")
            _he = float(input('What is your height? [6.2]: '))
            heig = pac.cvert_fttoin(_he)
            we = int(input('What is your weight in lbs?: '))
            loop =False # This will make the while loop to end as not value of loop is set to False
            return we, heig
            ## You can add your code or functions here
        elif choice =='2':
            print("You have selected that you \ndon't know any of the asked information")
            choice = input("Would you like to guess? [yes, no]: ")
            if choice == 'yes':
                ghe = float(input('What is your estimated height? [6.2]: '))
                gheig = pac.cvert_fttoin(ghe)
                gwe = int(input('What is your estimated weight in lbs?: '))
                # print("You are {0} {1}lbs".format(ghe, gwe))
                loop =False # This will make the while loop to end as not value of loop is set to False
                return gwe, gheig
            elif choice == 'no':
                print('Ok moving on....')
                loop =False # This will make the while loop to end as not value of loop is set to False
                return str('None'), str('None')
            ## You can add your code or functions here
        elif choice =='3':
            print("You've selected that you \nat least know you height.")
            he = float(input('What is your height? [6.2]: '))
            heig = pac.cvert_fttoin(he)
            dwe = 'None'
            loop = False
            return dwe, int(heig)
            ## You can add your code or functions here
        elif choice =='4':
            print("You've selected that you at \nleast   know your weight.")
            dhe = 'None'
            we = int(input('What is your weight in lbs?: '))
            loop = False
            return we, dhe
            ## You can add your code or functions here
        elif choice =='5':
            print("You've selected that you don't wish to share")
            ## You can add your code or functions here
            loop =False # This will make the while loop to end as not value of loop is set to False
            return str('None'), str('None')
        else:
            ## Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")
            loop = True

def GendChoices():
    loop = True

    while loop:  ## While loop which will keep going until loop = False

        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            cho = 'male'
            print("You have selected {}.".format(cho))
            loop =False # This will make the while loop to end as not value of loop is set to False
            return cho
            ## You can add your code or functions here
        elif choice =='2':
            cho = 'female'
            print("You have selected {}.".format(cho))
            loop = False
            return cho
            ## You can add your code or functions here
        elif choice =='3':
            cho = 'transgender male'
            print("You have selected {}.".format(cho))
            loop = False
            return cho
            ## You can add your code or functions here
        elif choice =='4':
            cho = 'transgender woman'
            print("You have selected {}.".format(cho))
            loop = False
            return cho
            ## You can add your code or functions here
        elif choice =='5':
            print("You've selected that you don't wish to share")
            ## You can add your code or functions here
            loop =False # This will make the while loop to end as not value of loop is set to False
            return str('None')
        else:
            ## Any integer inputs other than values 1-5 we print an error message
            input("Wrong key selection. Enter any key to try again..")
            loop = True

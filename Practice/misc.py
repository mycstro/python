#This program will do a couple of things.
#The first time it is run, it will request that you add a password. Once you do, it will change the check_e$
#Every subsequent time, it will check the password in the other file and then match user input.
#If user input is correct it will display a joke.
#If user input is incorrect it will exit the program.

#Function to help the user pick a password
def pick_password():
        file = '/home/vhx/Documents/code/pydata_test/password_dbs/pswd.txt'
        print ('Please pick a password.')
        password = input()
        target = open(file, 'w')
        target.write(password)
        file = '/home/vhx/Documents/code/pydata_test/password_dbs/existence_check.txt'
        target = open(file, 'w')
        target.write('YES')
        file.close()
        
def password_check():
        file = '/home/vhx/Documents/code/pydata_test/password_dbs/pswd.txt'
        pwd_check = open(file).read()
        userpass = raw_input('Please input a password.\n')
        if userpass == pwd_check:
                print 'Password accepted!'
                print 'Ready for the joke?'
                raw_input()
                print 'Why did the fly fly? Because the spider spied her!'
        elif userpass != pwd_check:
                print 'Sorry, wrong password.\n'
                exit()
        else:
                print 'Invalid syntax.'
                exit()
                
#location of password existence check file
EC = '/home/vhx/Documents/code/pydata_test/password_dbs/existence_check.txt'
PWD = '/home/vhx/Documents/code/pydata_test/password_dbs/pswd.txt' #Location of password file

pswd_exist = open(EC).read() #Checking to see if the password exists
if pswd_exist == 'YES':
        pass
else:
        pick_password() #If it doesn't, user will pick a password

#Checking for password
password_check()

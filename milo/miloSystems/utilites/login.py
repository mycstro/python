from __future__ import print_function
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
from dbMySql.conMySql import ConnDB
import getpass


_conn1 = ConnDB().dbconnect()
cursor = MySQLCursor(_conn1)

loop = 'true'
while(loop == 'true'):
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ')
    if(cursor.execute("SELECT * FROM `users` = '" + username + "' AND `password`" + password + "'")):
        _conn1.commit()
        print("Logged In")
    else:
        _conn1.commit()
        print("The username or password you've entered is incorrect.")
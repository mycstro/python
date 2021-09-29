from __future__ import print_function
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
from dbMySql.conMySql import ConnDB
import sys

def exec_sql_script(scriptname):
    scriptfilename = scriptname
    c = ConnDB()

    try:
        print("\nOpening connection...")
        _conn1 = c.dbconnect()
        cursor = MySQLCursor(_conn1)

        print("Reading Script...")
        scriptFile = open(scriptfilename, 'r')
        script = scriptFile.read()
        scriptFile.close()

        print("Running Script...")
        cursor. execute(script)

        _conn1.commit()
        print("Changes successfully committed\n")

    except Error as e:
        print("Something went wrong:")
        print(e)
    finally:
        print("\nClosing DB")
        c.dbclose()


# exec_sql_script('factoryDB.sql')
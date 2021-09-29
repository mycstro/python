from mysql.connector import MySQLConnection as mysqlc, Error
from dbMySql.parserMySql import read_db_config
from iniParser import read_config


class ConnDB:

    _dbconfig = read_config
    _f = 'config.ini'

    def __init__(self):
        print("Starting database connector")

    def dbclose(self):

        """Close connection to MySQL database. """
        try:
            _config = ConnDB._dbconfig(ConnDB._f, 'mysql')
            conn = mysqlc(**_config)
            conn.close()
            if conn.is_connected():
                print("Database connection remains!")
            else:
                print("Database connection is closed")
        except Error as error:
            print(error)

    def dbconnect(self):
        """Connects to MySQL database. """
        try:
            print('Connecting to database...')
            _config = ConnDB._dbconfig(ConnDB._f, 'mysql')
            conn = mysqlc(**_config)
            if conn.is_connected():
                print("Database is connected.")
                return conn
            else:
                print('Database connection failed')
        except Error as error:
            print(error)

        finally:
            print('Database connection is open')

# if __name__ == '__main__':
#     c = ConnDB()
#     c.dbconnect()
#     c.dbclose()

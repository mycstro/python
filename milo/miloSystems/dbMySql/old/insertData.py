from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
from dbMySql.conMySql import ConnDB


class InsertDB:

    def __init__(self):
        print("Inserting into database")

    def insert_user(username, email, password,):
        query = "INSERT INTO users(username,email,password) " \
                "VALUES(%s,%s,%s)"
        args = (username, email, password)

        c = ConnDB()

        try:
            print("Attempting to insert, ", username)
            _conn1 = c.dbconnect()
            cursor = MySQLCursor(_conn1)
            cursor.execute(query, args)

            if cursor.lastrowid:
                print(username, "was inserted \ncorrectly on row id" , cursor.lastrowid)
            else:
                print('last insert id not found')

            _conn1.commit()
        except Error as error:
            print("There was an error inserting, ", username, error)
            # print(error)

        finally:
            c.dbclose()

    def insert_book(title, isbn):
        query = "INSERT INTO books(title,isbn) " \
                "VALUES(%s,%s)"
        args = (title, isbn)

        c = ConnDB()

        try:
            _conn1 = c.dbconnect()
            cursor = MySQLCursor(_conn1)
            cursor.execute(query, args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

            _conn1.commit()
        except Error as error:
            print(error)

        finally:
            c.dbclose()

    def insert_books(books):
        query = "INSERT INTO books(title,isbn) " \
                "VALUES(%s,%s)"

        c = ConnDB()

        try:
            _conn1 = c.dbconnect()
            cursor = MySQLCursor(_conn1)
            cursor.executemany(query, books)

            _conn1.commit()
        except Error as e:
            print('Error:', e)

        finally:
            c.dbclose()

# def insertUserTest():
#     _inDB = InsertDB.insert_user
#     _inDB('mycstro', 'mycstro@yahoo.com', 'myc2367')
#
# def insertBookTest():
#     _inBDB = InsertDB.insert_book
#     _inBDB('A Sudden Light', '9781439187036')
#
# def insertBooksTest():
#     _inBDBS = InsertDB.insert_books
#     books = [('Harry Potter And The Order Of The Phoenix', '9780439358071'),
#              ('Gone with the Wind', '9780446675536'),
#              ('Pride and Prejudice (Modern Library Classics)', '9780679783268')]
#     _inBDBS(books)
#
# if __name__ == '__main__':
#     insertUserTest()
#     insertBookTest()
#     insertBooksTest()
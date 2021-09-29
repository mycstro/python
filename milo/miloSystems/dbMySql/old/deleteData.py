from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
from dbMySql.conMySql import ConnDB


class DeleteDB:

    def __init__(self):
        print("Starting deleter")

    def deleteUser(userid):
        c = ConnDB()

        query = "DELETE FROM users WHERE userid = %s"
        args = (userid)


        try:
            # connect to the database server
            _conn1 = c.dbconnect()
            cursor = MySQLCursor(_conn1)
            print("Locating user with id....", userid)
            cursor.execute(query, (userid,))

            # accept the change
            print("Delecting user with id....", userid)
            _conn1.commit()

        except Error as error:
            print(error)

        finally:
            c.dbclose()

    def delete_book(book_id):
        c = ConnDB()

        query = "DELETE FROM books WHERE id = %s"

        try:
            # connect to the database server
            _conn1 = c.dbconnect()
            cursor = MySQLCursor(_conn1)
            print("Locating book with id....", book_id)
            cursor.execute(query, (book_id,))

            # accept the change
            print("Delecting book with id....", book_id)
            _conn1.commit()

        except Error as error:
            print(error)

        finally:
            c.dbclose()


# if __name__ == '__main__':
#     ddb = DeleteDB
#     ddb.delete_book(102)
#     ddb.deleteUser(17)
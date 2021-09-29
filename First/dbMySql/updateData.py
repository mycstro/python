from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
from dbMySql.conMySql import ConnDB


class UpdateDB:

    def __init__(self):
        print("Preparing to update records.....")


    def update_book(book_id, title):


        # read database configuration
        c = ConnDB()

        # prepare query and data
        query = """ UPDATE books
                    SET title = %s
                    WHERE id = %s """

        data = (title, book_id)

        try:
            _conn1 = c.dbconnect()
            cursor = MySQLCursor(_conn1)
            cursor.execute(query, data)

            # accept the changes
            _conn1.commit()
            print('Data committed')

        except Error as error:
            print(error)

        finally:
            c.dbclose()


# if __name__ == '__main__':
#     u = UpdateDB
#     u.update_book(37, 'The Giant on the Hill *** TEST ***')
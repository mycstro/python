from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
from dbMySql.conMySql import ConnDB


class FetchDB:

    def __init__(self):
        print("Waking Fido for fetch....")

    def currentDB(self):
        _c = ConnDB()

        try:
            _conn1 = _c.dbconnect()
            cursor = MySQLCursor(_conn1)
            cursor.execute("select database()")

            dbname = cursor.fetchone()[0]

            while dbname is not None:
                # print(dbname)
                dbname = cursor.fetchone()
                return dbname

        except Error as e:
            # print(e)
            return e

        finally:
            _c.dbclose()

    def query_with_fetchone(self, select):
        _c = ConnDB()

        try:
            _conn1 = _c.dbconnect()
            cursor = MySQLCursor(_conn1)
            cursor.execute(select)

            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()
                return row

        except Error as e:
            print(e)
            return e

        finally:
            _c.dbclose()

    def query_with_fetchall(self, select):
        _c = ConnDB()

        try:
            _conn1 = _c.dbconnect()
            cursor = MySQLCursor(_conn1)
            cursor.execute(select)
            rows = cursor.fetchall()

            print('Total Row(s):', cursor.rowcount)
            for row in rows:
                print(row)

        except Error as e:
            print(e)

        finally:
            _c.dbclose()

    def iter_row(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def query_with_fetchmany(self, select):
        _c = ConnDB()
        _f = FetchDB

        try:
            _conn1 = _c.dbconnect()
            cursor = MySQLCursor(_conn1)
            cursor.execute(select)

            for row in _f.iter_row(cursor, 10):
                print(row)

        except Error as e:
            print(e)

        finally:
            _c.dbclose()


# if __name__ == '__main__':
#     f = FetchDB()
#     f.currentDB()
#     f.query_with_fetchone("SELECT * FROM books")
#     for i in range(1, 6):
#         f.query_with_fetchone("Select * From books WHERE ID = {}".format(i))
#     f.query_with_fetchall("SELECT * FROM users")
#     f.query_with_fetchall("SELECT * FROM books")
#     f.query_with_fetchmany("SELECT * FROM books")
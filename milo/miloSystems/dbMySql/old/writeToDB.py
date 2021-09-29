from __future__ import print_function
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
from dbMySql.conMySql import ConnDB
import dbMySql.tables as t


class WriteToDB:
    def __init__(self):
        self._conn1 = ConnDB().dbconnect()


    def create_database(self, db_name):
        cursor = MySQLCursor(self._conn1)
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
            print("\nCreated database: {}.".format(db_name))
        except Error as error:
            print("Failed creating database: {}".format(error))
            # exit(1)

    def modify_table(self, db_name, table):
        cursor = MySQLCursor(self._conn1)
        ConnDB.database = db_name
        for name, ddl in table.items():
            try:
                print("\nModifying table {}:... ".format(name), end='')
                cursor.execute("USE {}".format(ConnDB.database))
                cursor.execute(ddl)
            except Error as err:
                print(err.msg)
            else:
                print("DONE")

        cursor.close()
        ConnDB().dbclose()

    def drop_database(self, db_name):
        cursor = MySQLCursor(self._conn1)

        try:
            ConnDB.database = db_name
        except self._conn1.Error as err:
            print(err.msg)
            exit(1)
        try:
            print("Deleting Database {}:... ".format(ConnDB.database), end='')
            cursor.execute("DROP DATABASE {}".format(ConnDB.database))
        except Error as err:
            print("Something went wrong!".format(err.msg))
        else:
            print("DONE")

#
# GTABLES = {}
# DTABLES = {}
# GTABLES['users'] = (
#     "CREATE TABLE `users` ("
#     "  `id` int NOT NULL AUTO_INCREMENT,"
#     "  `username` varchar(16) NOT NULL,"
#     "  `email` varchar(50) DEFAULT NULL,"
#     "  `password` varchar(16) NOT NULL,"
#     "  `usercreation` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
#     "  PRIMARY KEY (`id`, `username`),"
#     "  UNIQUE KEY `id` (`id`)"
#     ") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;")
# DTABLES['users'] = (
#     "DROP TABLE `users`"
# )
#
# DTABLES['birth_locations'] = (
#     "START TRANSACTION;"
#     "SET @id_to_delete = <{row_id}>;"
#     "DELETE FROM users_profiles"
#         "USING profiles, users_profiles, birth_locations"
#         "WHERE `birth_locations`.`id` = `profiles`.`birth_address_id`"
#               "AND `profiles`.`id` = `users_profiles`.`profile_id`"
#               "AND birth_locations.id = @id_to_delete;"
#     "DELETE FROM profiles"
#         "USING profiles, birth_locations"
#         "WHERE `birth_locations`.`id` = `profiles`.`birth_address_id`"
#               "AND birth_locations.id = @id_to_delete;"
#     "DELETE FROM birth_locations"
#         "USING birth_locations"
#         "WHERE birth_locations.id = @id_to_delete;"
#     "COMMIT;"
#     )
#
# modify_table("milo_defaults", GTABLES)
# modify_table("milo_defaults", DTABLES)
# drop_database("milo_defaults")
# create_database("milo_defaults")

#
# WriteToDB().drop_database("milo_defaults")
# WriteToDB().create_database("milo_defaults")
# WriteToDB().modify_table("milo_defaults", t.TABLES)
# WriteToDB().modify_table("milo_defaults", t.ALTERS)
# WriteToDB().modify_table("milo_defaults", t.INSERTS)

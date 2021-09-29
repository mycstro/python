from tkinter import *
import tkinter.ttk as ttk
from mysql.connector.cursor import MySQLCursor
from dbMySql.conMySql import ConnDB

from dbMySql import c, f, d, u, i

root = Tk()
root.geometry("400x240")
tree = ttk.Treeview(root)
_f=f()
tree["columns"] = ("one", "two")
tree.column("#0", width=50)
tree.column("one", width=200)
tree.column("two", width=200)
tree.heading("#0", text='ID', anchor='w')
tree.column("#0", anchor="w")
tree.heading("one", text="Title")
tree.heading("two", text="ISBN")
_c = ConnDB()
_conn1 = _c.dbconnect()
cursor = MySQLCursor(_conn1)
cursor.execute("Select * From books")
row = cursor.fetchone()
for row in range(1, 10):
    row = cursor.fetchone()
    # print(row)
    bid = row[0]
    bna = row[1]
    bis = row[2]
    tree.heading("two", text="Numbers")

    tree.insert("", "end", text=bid, values=(bna, bis)), tree.pack()
# tree.insert("", i, text=i, values=(nm, vot, percent)), tree.pack()
root.mainloop()
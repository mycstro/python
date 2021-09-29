'''
Created on Mar 21, 2016

@author: Bill Begueradj
'''
import tkinter
import tkinter.ttk
from mysql.connector.cursor import MySQLCursor
from dbMySql.conMySql import ConnDB

from dbMySql import c, f, d, u, i

class Begueradj(tkinter.Frame):
    '''
    classdocs
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Test 10")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="grey")


        # Define the different GUI widgets
        self.dose_label = tkinter.Label(self.parent, text = "Book Title:")
        self.dose_entry = tkinter.Entry(self.parent)
        self.dose_label.grid(row = 0, column = 0, sticky = tkinter.W)
        self.dose_entry.grid(row = 1, column = 0, sticky = tkinter.W)

        self.modified_label = tkinter.Label(self.parent, text = "ISBN")
        self.modified_entry = tkinter.Entry(self.parent)
        self.modified_label.grid(row = 0, column = 1, sticky = tkinter.W)
        self.modified_entry.grid(row = 1, column = 1, sticky = tkinter.W)

        # Set the treeview
        self.tree = tkinter.ttk.Treeview( self.parent, columns=('Book Title', 'ISBN'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Book Title')
        self.tree.heading('#2', text='ISBN')
        self.tree.column("#0", width=50)
        self.tree.column("#1", width=200)
        self.tree.column("#2", width=200)
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        self.tree.column('#0', stretch=tkinter.NO)
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # Initialize the counter
        self.i = 0

        self.submit_button = tkinter.Button(self.parent, text = "Insert", command = self.insert_data)
        self.submit_button.grid(row = 2, column = 1, sticky = tkinter.E)
        self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.parent.quit)
        self.exit_button.grid(row = 2, column = 2, sticky = tkinter.E)

    def insert_data(self):
        """
        Insertion method.
        """
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
            self.treeview.insert('', "end", text=bid, values=(bna, bis))
        # self.treeview.insert('', 'end', text="Item_"+str(self.i), values=(self.dose_entry.get()+" mg", self.modified_entry.get()))
        # Increment counter
        self.i = self.i + 1

def main():
    root=tkinter.Tk()
    d=Begueradj(root)
    root.mainloop()

if __name__=="__main__":
    main()
#######################
# File: tkoutput.py
# Author: A.J. Gauld
# Date: September 2001
#
from tkinter import *
import sys
import dbMySql as db

class Display(Frame):
    ''' Demonstrate python interpreter output in Tkinter Text widget

type python expression in the entry, hit DoIt and see the results
in the text pane.'''

    def __init__(self, parent=0):
        Frame.__init__(self, parent)
        self.entry = Entry(self)
        self.entry.pack()
        self.doIt = Button(self, text="DoIt", command=self.onEnter)
        self.doIt.pack()
        self.output = Entry(self)
        self.output.pack()
        sys.stdout = self
        self.pack()

    def onEnter(self):
        eval(self.entry.get())

    def write(self, txt):
        self.output.insert(END, str(txt))

    def hello(arg):
        t = arg
        print(t)


if __name__ == '__main__':

    conn = db.c()
    connect = conn.dbconnect
    close = conn.dbclose
    fete = db.f()
    database = fete.currentDB
    h = Display.hello

    Display().mainloop()

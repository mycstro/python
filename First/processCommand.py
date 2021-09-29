from dbMySql import c, f, d, u, i
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    from tkinter import filedialog

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import treeViews

# def set_Tk_var():
#     global stv22
#     stv22 = StringVar()
#     global che44
#     che44 = StringVar()
#     global che45
#     che45 = StringVar()
#     global spinbox
#     spinbox = StringVar()
#     global che66
#     che66 = StringVar()
#     global entry1txt
#     entry1txt = StringVar()
#     global che67
#     che67 = StringVar()


def process_command(text):
    ''' Given a string, returns a string in response. '''
    text = text.strip().lower()
    if text == 'dbconnect':
        t = c()
        t.dbconnect()
    elif text == 'dbclose':
        t = c()
        t.dbclose()
    elif text in {'currentdb', 'database', 'current database'} :
        t = f()
        t.currentDB()
    elif text == 'fetch':
        print('ok')
        t = f()
        qu = input("Select. [one, many, all]: ")
        quan = qu.strip().lower()
        tabl = input("Which table ['users', 'books']: ")
        idnum = input("What is the ID number: ")
        qry = "Select * From {} WHERE ID = {}".format(tabl, idnum)
        if quan == 'one':
            t.query_with_fetchone(qry)
        if quan == 'many':
            t.query_with_fetchmany(qry)
        if quan == 'all':
            t.query_with_fetchall(qry)
    elif text in {'quit', 'exit'}:
        # clear the input field
        try:
            print('Attempting to quit')
        except AttributeError:
            pass
    else:
        print('Unknown Command')

# def init(top, gui, *args, **kwargs):
#     global w, top_level, root
#     w = gui
#     # treeViews.set_Tk_var()
#     top_level = top
#     # treeViews.init(root, top)
#     root = top

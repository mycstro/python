import dbMySql as db
try:
    import tkinter as tk
except AttributeError:
    print('AttributeError detected. ')
    import Tkinter as tk
else:
    print('Tkinter imported. ')

class First:

    def __init__(self, app):
        self.app = app

    ##### create new window
    #set app title
        app.title("Mycstro")
    #set app min size
        app.minsize(450, 450)
    #set window background to hex code '#a2dbcd'
        app.config(background="#a1dbcd")

    # Todo-myc fix - set app icon
    # app.iconbitmap(default='icon.ico')
    #root.tk.call('wm', 'iconbitmap', self._w, '-default', 'iconfile.ico' )
    #photo = tk.PhotoImage(file="header.gif")
    #w = tk.Label(app, image=photo)
    #w.pack()

        def insertUserTest():
            _inDB = db.i.insert_user
            # _inDB = InsertDB.insert_user
            _inDB('mycstro', 'mycstro@yahoo.com', 'myc2367')

        def insertBookTest():
            _inBDB = db.i.insert_book
            _inBDB('A Sudden Light', '9781439187036')

        def insertBooksTest():
            _inBDBS = db.i.insert_books
            books = [('Harry Potter And The Order Of The Phoenix', '9780439358071'),
                     ('Gone with the Wind', '9780446675536'),
                     ('Pride and Prejudice (Modern Library Classics)', '9780679783268')]
            _inBDBS(books)


        #create a label for the instructions
        lblInst = tk.Label(app, text="Please login to continue:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
        #and pack it into the window
        lblInst.pack()

        #create the widgets for entering a username
        lblUsername = tk.Label(app, text="Username:", fg="#383a39", bg="#a1dbcd")
        entUsername = tk.Entry(app)
        #and pack them into the window
        lblUsername.pack()
        entUsername.pack()

        #create the widgets for entering a username
        lblPassword = tk.Label(app, text="Password:", fg="#383a39", bg="#a1dbcd")
        entPassword = tk.Entry(app)
        #and pack them into to the window
        lblPassword.pack()
        entPassword.pack()

        #create a button widget called btn
        btn = tk.Button(app, text="Login", fg="#a1dbcd", bg="#383a39")
        #pack the widget into the window
        btn.pack()


# if __name__ == '__main__':
app = tk.Tk()
first_gui = First(app)
app.mainloop()

    # conn = db.c()
    # conn.dbconnect()
    # conn.dbclose()
    # db.d.delete_book(102)
    # db.d.deleteUser(17)
    # insertUserTest()
    # insertBookTest()
    # insertBooksTest()
    # fete = db.f()
    # fete.currentDB()
    # fete.query_with_fetchone("SELECT * FROM books")
    # fete.query_with_fetchall("SELECT * FROM users")
    # fete.query_with_fetchall("SELECT * FROM books")
    # fete.query_with_fetchmany("SELECT * FROM books")
    # db.u.update_book(37, 'The Giant on the Hill *** TEST ***')

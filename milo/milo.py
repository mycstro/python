#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from miloSystems.dbMySql.conMySql import ConnDB, FetchDB
from tkinter import *
from PIL import ImageTk, Image

milo_version = '0.0.1'

db = ConnDB().dbconnect()
cursor = db.cursor()


def logintodb(user, passw):
    # Query table in the database
    savequery = """SELECT users.username 
        FROM milo_defaults.users 
        WHERE users.username = '{}' AND users.password = '{}';""".format(user, passw)
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchone()
        print(myresult)
    except:
        db.rollback()
        print("Error occured")
        sys.exit()

    if myresult:
        print("LogIn is good!")
        my_error.config(text="Login successfully. \nWelcome {}".format(myresult))
        welcome()
    else:
        print("LogIn was unsuccessful!")
        my_error.config(text="The credentials entered is not in our system.")


def usertodb():
    INSERTS = {}
    savequery = INSERTS['users'] = (
        "INSERT INTO `milo_defaults`.`users`"
        "   (`id`, `username`, `email`, `password`)"
        "   VALUES"
        "   ('2', 'mycstro', 'mycstro@vspace.com', 'myc2367');")
    try:
        cursor.execute("INSERT INTO users VALUES (:username, :email, :password)",
                       {
                           'username': un_entry.get(),
                           'email': em_entry.get(),
                           'password': pw_entry.get()
                       })
        db.commit()
        db.close()
        welcome()
    except:
        print("error")


class LoginWindow(Frame):
    def __init__(self):
        super().__init__()

        login_btn.destroy()
        self.iniUI()

    def iniUI(self):
        self.master.title("LogIn")
        self.pack(fill=BOTH, expand=1)

        global frame1
        frame1 = Frame(self)
        frame1.pack(fill=X)

        # Define Entry Boxes
        print("Creeating LogIn Screen.....")
        global un_entry, pw_entry
        un_entry = Entry(frame1, font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
        un_entry.insert(0, "username")
        un_entry.pack(side=TOP, padx=5, pady=5)

        pw_entry = Entry(frame1, font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
        pw_entry.insert(0, "password")
        pw_entry.pack(side=TOP, padx=5, pady=5)

        # Define Button
        global login_btn, register_btn
        login_btn = Button(frame1, text="Login", font=("Helvetica", 20), width=15, fg="#336d92", command=submitact)
        login_btn.pack(side=LEFT, padx=5, pady=5)
        # login_btn_window = my_canvas.create_window(36, 470, anchor="nw", window=login_btn)

        register_btn = Button(frame1, text="Register", font=("Helvetica", 20), width=15, fg="#336d92", command=RegisterWindow)
        register_btn.pack(side=LEFT, padx=5, pady=5)

        # Bind the entry boxes
        un_entry.bind("<Button-1>", self.entry_clear)
        pw_entry.bind("<Button-1>", self.entry_clear)
        pw_entry.bind("<Return>", self.returnact)

    def returnact(self, e):
        submitact()

    # Define entry_clear function
    def entry_clear(self, e):
        if un_entry.get() == 'username' or pw_entry.get() == 'password':
            un_entry.delete(0, END)
            pw_entry.delete(0, END)
            # change text to stars
            un_entry.config(show="")
            pw_entry.config(show="*")

def submitact():
    global un_entry, pw_entry
    print(un_entry.get())
    _user = ""
    try:
        _user = un_entry.get()
        print("Checking for username {}...".format(_user))
    except NameError:
        my_error.config(text="Your Username is incorrect.")

    _passw = pw_entry.get()
    if not _user:
        print("No user")
        if not _passw:
            print("No user and password")
            my_error.config(text="Please enter the correct credentials for your account")
    else:
        print("Attempting to log in...")
        my_error.config(text="Logging in {}".format(_user))
        logintodb(_user, _passw)


def registeruser():
    print("Creating Registration")

    my_error.config(text="Registering User!")


def welcome():
    # Create welcome screen
    print("Creating Welcome")
    frame1.pack_forget()
    #frame1.destroy()

    # Add a welcome message
    data = un_entry.get()
    print(data)
    message = "Welcome \n{}".format(un_entry.get())
    my_canvas.create_text(160, 160, text=message, font=("Helvetica", 40), fill="white")


def move(e):
    # e.x
    # e.y
    global img
    img = PhotoImage(file="graphics/assets/images/capricorn.png")
    my_canvas.create_image(e.x, e.y, image=img)
    my_error.config(text="Coordinates x: " + str(e.x) + " y: " + str(e.y))


class RegisterWindow(Frame):
    def __init__(self):
        super().__init__()
        self.iniUI()

    def iniUI(self):
        self.master.title("Registration")
        self.pack(fill=BOTH, expand=1)

        global frame1
        frame1.pack_forget()
        my_canvas.destroy()
        my_error.pack_forget()

        frame1 = Frame(self)
        frame1.grid(column=4, row=6, columnspan=2, padx=5, pady=5)

        # Create
        global un_entry, pw_entry, em_entry, f_name, l_name, address, zipcode
        un_entry = Entry(frame1, font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
        un_entry.insert(0, "Username")
        un_entry.grid(row=1, column=0, padx=5, pady=(5, 0))
        pw_entry = Entry(frame1, font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
        pw_entry.insert(0, "password")
        pw_entry.grid(row=1, column=1, padx=5, pady=(5, 0))
        em_entry = Entry(frame1, font=("Helvetica", 24), width=28, fg="#336d92", bd=0)
        em_entry.insert(0, "Email")
        em_entry.grid(row=2, column=0, padx=5, pady=(5, 0))
        f_name = Entry(frame1, font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
        f_name.insert(0, "First Name")
        f_name.grid(row=3, column=0, padx=5, pady=(5, 0))
        l_name = Entry(frame1, font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
        l_name.insert(0, "Last Name")
        l_name.grid(row=3, column=1, padx=5, pady=(5, 0))
        address = Entry(frame1, font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
        address.insert(0, "address")
        address.grid(row=4, column=0, padx=5, pady=(5, 0))
        zipcode = Entry(frame1, font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
        zipcode.insert(0, "zipcode")
        zipcode.grid(row=5, column=1, padx=5, pady=(5, 0))

        # Create Submit Button
        submit_btn = Button(frame1, text="Add Record To Database", command=registeruser)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        # Bind the entry boxes
        un_entry.bind("<Button-1>", self.entry_clear)
        pw_entry.bind("<Button-1>", self.entry_clear)
        zipcode.bind("Enter", registeruser)

        # Define entry_clear function

    def entry_clear(self, e):
        if un_entry.get() == 'username' or pw_entry.get() == 'password':
            un_entry.delete(0, END)
            pw_entry.delete(0, END)
            em_entry.delete(0, END)
            f_name.delete(0, END)
            l_name.delete(0, END)
            address.delete(0, END)
            zipcode.delete(0, END)
            # change text to stars
            pw_entry.config(show="*")


# Change to the current directory
print("Setting Directory...")
os.chdir(os.path.dirname(os.path.realpath(__file__)))


def main():
    print("Configurating TK")
    root = Tk()
    # app = LoginWindow()
    root.title('Milo')
    root.iconbitmap('graphics/assets/favicon.ico')

    # Designate Height and Width of our app
    app_width = 500
    app_height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # make sure app can't be resized
    root.resizable(width=True, height=True)

    w = 500
    h = 400
    x = w / 2
    y = h / 2

    global my_canvas
    # Define Canvas
    my_canvas = Canvas(root, width=w, height=h, bd=0, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)

    # Define Grid
    # my_grid = Canvas(my_canvas)
    # my_grid.grid(row=1, column=0, sticky='ew', columnspan=8, rowspan=8)

    # Define Background Image
    bg = ImageTk.PhotoImage(file="graphics/assets/images/background.png")

    # Put the image on the canvas
    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    # Add Image To Canvas
    global img
    img = PhotoImage(file="graphics/assets/images/capricorn.png")
    my_canvas.create_image(0, 0, anchor=NW, image=img)

    global my_error
    yv = "VSpace Version- {}".format(milo_version)
    my_error = Label(root, text=yv)
    my_error.pack(pady=20)

    my_canvas.bind('<B1-Motion>', move)

    # Define Button
    global login_btn
    login_btn = Button(root, text="Enter", font=("Helvetica", 20), width=15, fg="#336d92", command=LoginWindow)
    my_canvas.create_window(120, 470, anchor="nw", window=login_btn)

    print("Running Milo")
    root.mainloop()


if __name__ == '__main__':
    main()

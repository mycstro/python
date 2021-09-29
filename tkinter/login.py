try:
    import tkinter as tk
except AttributeError:
    print('AttributeError detected. ')
    import Tkinter as tk
else:
    print('Tkinter imported. ')

##### create new window
app = tk.Tk()
#set app title
app.title("Mycstro")
#set app min size
app.minsize(300, 150)
#set window background to hex code '#a2dbcd'
app.config(background="#a1dbcd")

# Todo-myc fix - set app icon
# app.iconbitmap(default='icon.ico')
#root.tk.call('wm', 'iconbitmap', self._w, '-default', 'iconfile.ico' )
#photo = tk.PhotoImage(file="header.gif")
#w = tk.Label(app, image=photo)
#w.pack()

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

app.mainloop()
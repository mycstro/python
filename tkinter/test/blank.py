#import Tkinter
from logging import root

try:
    import tkinter as tk
except AttributeError:
    print('AttributeError detected. ')
    import Tkinter as tk
else:
    print('Tkinter imported. ')

# class AppName(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)
#         self.grid()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.quitButton = tk.Button(self, text='Quit', command=self.quit)
#         self.quitButton.grid()

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

#print hello
def print_hello():
    print("hello")

#key down function
def click():
    entered_text=textentry.get() #this will collect the text from the text entry box
    output.delete(0.0, END)

#a function that adds 1 to the text of the label
def addClick():
    #this means that this function should
    #use the presses variable declared outside
    #of the function
    global presses
    #add one to presses
    presses += 1
    #update the label text with the new value of 'presses'
    lbl.configure(text=presses)

# a function that prints what's on the button
def printClick():
    #this function should
    #use the greet variable declared outside
    #of the function
    global greet
    #add greet variable
    greet = 'Hello'
    print_hello()
    #update the label text with the new value
    lbl.config(text=greet)

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

# #initially, the button hasn't been pressed
# presses = 0
#
# #create a label to display a message
# lbl = tk.Label(app, text=presses)
# lbl.pack()
#
# #create a new button, and provide an argument called 'command'
# #which in this case calls a function called 'callback'
# btn = tk.Button(app, text="Click Me", command=addClick)
# btn.pack()

# greet = 0
#
# lbl = tk.Label(app, text=greet)
# lbl.pack()
#
# helloLabel = tk.Label(app, text="Thank You", bg="#a1dbcd")
# helloLabel.pack()
#
# helloButton = tk.Button(app, text="Print Hello", command=printClick(), fg="#a1dbcd", bg="#383a39")
# helloButton.pack()

#draw the window, and start the 'application'
app.mainloop()
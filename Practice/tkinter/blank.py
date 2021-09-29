try:
    import tkinter as tk
except AttributeError:
    print('AttributeError detected. ')
    import Tkinter as tk
else:
    print('Tkinter imported. ')

class PrintHello:

    def getandreplace(self):
        """replace x with * and ÷ with /"""
        self.v = "Welcome"
        # self.v.replace("Welcome", "hello")


    def print_hello(self):
        tk.tkMessageBox.showinfo("hello")
        print("hello")

    def __init__(self, master):
        """Constructor method"""
        master.title('Mycstro')
        # master.geometry()
        master.minsize(300, 300)


        self.e = tk.Entry(master)
        self.e.focus_set()  # Sets focus on the input text area

        helloLabel = tk.Label(app, text=self.v)
        helloButton = tk.Button(app, text="Print hello", command=lambda: self.print_hello())

        helloButton.pack()
        helloLabel.pack()

app = tk.Tk()
obj = PrintHello(app)  # object instantiated
app.mainloop()
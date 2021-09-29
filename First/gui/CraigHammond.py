# Craig Hammond 2016
from tkinter import *
from tkinter import ttk


class Application(Frame):

    def __init__(self, master):
        """ Initialize the Frame"""
        ttk.Frame.__init__(self, master)

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.btnConnect = ttk.Button(self, text="Search Symbol", command=self.search_symbol).grid(row=0, column=0,
                                                                                                  sticky=W)
        self.btnDisconnect = ttk.Button(self, text="Add data", command=self.add_data).grid(row=0, column=1, sticky=W)
        self.btnCancelMktData = ttk.Button(self, text='Remove All', command=self.remove_all).grid(row=0, column=2,
                                                                                                  sticky=W)
        self.button_edit = Button(self, font=('', 12), text="select row", width=7, command=self.add_data)
        self.button_edit.grid(row=0, column=4)

        # create Treeview widget to hold values in a table
        self.tv = ttk.Treeview(root)

        # create Treeview
        self.tv = ttk.Treeview(self, height=8)
        self.tv['columns'] = ('id', 'symbol', 'price', 'trigger', 'shares', 'side', 'type', 'status', 'fill')
        self.tv.heading("#0", text='Time', anchor='w')
        self.tv.column("#0", stretch=NO, width=5, anchor="w")
        self.tv.heading('id', text='ID')
        self.tv.column('id', anchor='center', width=70)
        self.tv.heading('symbol', text='Symbol')
        self.tv.column('symbol', anchor='center', width=70)
        self.tv.heading('price', text='Price')
        self.tv.column('price', anchor='center', width=70)
        self.tv.heading('trigger', text='Trigger')
        self.tv.column('trigger', anchor='center', width=70)
        self.tv.heading('shares', text='Shares')
        self.tv.column('shares', anchor='center', width=100)
        self.tv.heading('side', text='Side')
        self.tv.column('side', anchor='center', width=70)
        self.tv.heading('type', text='Type')
        self.tv.column('type', anchor='center', width=70)
        self.tv.heading('status', text='Status')
        self.tv.column('status', anchor='center', width=100)
        self.tv.heading('fill', text='Fill')
        self.tv.column('fill', anchor='center', width=70)
        self.tv.bind('<ButtonRelease-1>', self.select_item)
        self.tv.grid(row=1, column=0, columnspan=6, padx=5, pady=5)
        self.treeview = self.tv
        ##        self.ysb = ttk.Scrollbar(self, orient='vertical', command=self.tv.yview)
        ##        self.xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tv.xview)
        ##        self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
        ##        self.ysb.grid(row=1, column=7, sticky='ns')
        ##        self.xsb.grid(row=2, column=0, sticky='ew')

        ttk.Style().configure("Treeview", font=('', 11), background="#383838",
                              foreground="white", fieldbackground="yellow")

        self.tv.insert("", "end", text="Person",
                       values=("1254", "MSFT", "39.39", "", "0/200", "BUY", "LMT", "Filled", "39.39"), tags='hot')
        self.tv.insert("", "end", text="Animal",
                       values=("1255", "MSFT", "39.58", ".10", "0/200", "SELL", "TRAIL", "PreSubmitted", "0.00"),
                       tags='cold')
        self.tv.insert("", "end", text="Name",
                       values=("1256", "MSFT", "39.58", "", "0/200", "SELL", "LMT", "Submitted", "0.00"), tags='pizza')
        self.tv.insert("", "end", text="Evil Corp",
                       values=("1258", "NFLX", "102.55", "", "0/300", "SELL", "LMT", "Submitted", "0.00"), tags='tacos')

    def select_item(self, a):  # added self and a (event)
        test_str_library = self.tv.item(self.tv.selection())  # gets all the values of the selected row
        print('The test_str = ', type(test_str_library), test_str_library,
              '\n')  # prints a dictionay of the selected row
        item = self.tv.selection()[0]  # which row did you click on
        print('item clicked ', item)  # variable that represents the row you clicked on
        print(self.tv.item(item)['values'][0])  # prints the first value of the values (the id value)

    def remove_all(self):
        pass

    def search_symbol(self):
        pass

    def add_data(self):
        pass


root = Tk()
app = Application(root)
root.mainloop()
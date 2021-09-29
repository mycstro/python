

def defaultreeview(tree_widget):
    tree_space = tree_widget
    tree_space.place(relx=0.0, rely=0.06, relheight=0.93
            , relwidth=0.99)
    tree_space.configure(columns="Col1")
    tree_space.heading("#0", text="Tree")
    tree_space.heading("#0", anchor="center")
    tree_space.column("#0", width="213")
    tree_space.column("#0", minwidth="20")
    tree_space.column("#0", stretch="1")
    tree_space.column("#0", anchor="w")
    tree_space.heading("Col1", text="Col1")
    tree_space.heading("Col1", anchor="center")
    tree_space.column("Col1", width="213")
    tree_space.column("Col1", minwidth="20")
    tree_space.column("Col1", stretch="1")
    tree_space.column("Col1", anchor="w")

class ScrolledTreeView(object):
    def __init__(self, tree_widget):
        self.tree_view = tree_widget

    def write(self, string):
        self.tree_view.place(relx=0.0, rely=0.06, relheight=0.93
                , relwidth=0.99)
        self.tree_view.configure(columns="Col1")
        self.tree_view.heading("#0",text="Tree")
        self.tree_view.heading("#0",anchor="center")
        self.tree_view.column("#0",width="213")
        self.tree_view.column("#0",minwidth="20")
        self.tree_view.column("#0",stretch="1")
        self.tree_view.column("#0",anchor="w")
        self.tree_view.heading("Col1",text="Col1")
        self.tree_view.heading("Col1",anchor="center")
        self.tree_view.column("Col1",width="213")
        self.tree_view.column("Col1",minwidth="20")
        self.tree_view.column("Col1",stretch="1")
        self.tree_view.column("Col1",anchor="w")
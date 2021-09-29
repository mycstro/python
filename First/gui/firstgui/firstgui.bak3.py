#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.10
# In conjunction with Tcl version 8.6
#    Feb 03, 2018 08:42:27 AM

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

from gui.firstgui import firstgui_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    firstgui_support.set_Tk_var()
    top = New_Toplevel_1 (root)
    firstgui_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    firstgui_support.set_Tk_var()
    top = New_Toplevel_1 (w)
    firstgui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {DejaVu Sans Mono} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 0 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("602x447+997+244")
        top.title("New Toplevel 1")
        top.configure(highlightcolor="black")



        self.images = (

         PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                 KkoNUtRHpYYAADs= '''),

         PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),

         PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )

        self.style.element_create("close", "image", "img_close",
               ("active", "pressed", "!disabled", "img_closepressed"),
               ("active", "alternate", "!disabled",
               "img_closeactive"), border=8, sticky='')

        self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                     {"sticky": "nswe"})])
        self.style.layout("ClosetabNotebook.Tab", [
            ("ClosetabNotebook.tab",
              { "sticky": "nswe",
                "children": [
                    ("ClosetabNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("ClosetabNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("ClosetabNotebook.label", {"side":
                                      "left", "sticky": ''}),
                                    ("ClosetabNotebook.close", {"side":
                                        "left", "sticky": ''}),]})]})]})])

        PNOTEBOOK = "ClosetabNotebook" 

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.PNotebook1 = ttk.Notebook(top)
        self.PNotebook1.place(relx=0.02, rely=0.31, relheight=0.61
                , relwidth=0.97)
        self.PNotebook1.configure(width=300)
        self.PNotebook1.configure(style=PNOTEBOOK)
        self.PNotebook1_t0 = Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t0, padding=3)
        self.PNotebook1.tab(0, text="Home",compound="none",underline="-1",)
        self.PNotebook1_t1 = Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t1, padding=3)
        self.PNotebook1.tab(1, text="Book",compound="none",underline="-1",)
        self.PNotebook1_t2 = Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t2, padding=3)
        self.PNotebook1.tab(2, text="User",compound="none",underline="-1",)
        self.PNotebook1_t3 = Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t3, padding=3)
        self.PNotebook1.tab(3, text="Settings",compound="none",underline="-1",)
        self.PNotebook1_t4 = Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t4, padding=3)
        self.PNotebook1.tab(4, text="About",compound="none",underline="-1",)

        self.DBConnectButton = Button(self.PNotebook1_t0)
        self.DBConnectButton.place(relx=0.05, rely=0.08, height=26, width=76)
        self.DBConnectButton.configure(activebackground="#d9d9d9")
        self.DBConnectButton.configure(text='''Connect''')
        self.DBConnectButton.bind('<Button-1>', lambda e: firstgui_support.dbconnectbtn(e))

        self.DBCloseButton = Button(self.PNotebook1_t0)
        self.DBCloseButton.place(relx=0.22, rely=0.08, height=26, width=111)
        self.DBCloseButton.configure(activebackground="#d9d9d9")
        self.DBCloseButton.configure(text='''Close Connect''')
        self.DBCloseButton.bind('<Button-1>', lambda e: firstgui_support.dbclosebtn(e))

        self.Entry1 = Entry(self.PNotebook1_t0)
        self.Entry1.place(relx=0.47, rely=0.08,height=25, relwidth=0.36)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(selectbackground="#c4c4c4")

        self.Button1 = Button(self.PNotebook1_t0)
        self.Button1.place(relx=0.86, rely=0.08, height=26, width=59)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Enter''')
        self.Button1.bind('<Button-1>', lambda e: firstgui_support.enterbtn(e))

        self.TPanedwindow1 = ttk.Panedwindow(self.PNotebook1_t0
                , orient="horizontal")
        self.TPanedwindow1.place(relx=0.03, rely=0.24, relheight=0.72
                , relwidth=0.95)
        self.TPanedwindow1.configure(width=200)
        self.TPanedwindow1_p1 = ttk.Labelframe(width=96, text='')
        self.TPanedwindow1.add(self.TPanedwindow1_p1)
        self.TPanedwindow1_p2 = ttk.Labelframe(text='Pane 2')
        self.TPanedwindow1.add(self.TPanedwindow1_p2)
        self.__funcid0 = self.TPanedwindow1.bind('<Map>', self.__adjust_sash0)

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.Scrolledtreeview1 = ScrolledTreeView(self.TPanedwindow1_p1)
        self.Scrolledtreeview1.place(relx=0.0, rely=0.06, relheight=0.93
                , relwidth=0.99)
        self.Scrolledtreeview1.configure(columns="Col1")
        self.Scrolledtreeview1.heading("#0",text="Tree")
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="213")
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="w")
        self.Scrolledtreeview1.heading("Col1",text="Col1")
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="213")
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="w")

        self.Label1 = Label(self.TPanedwindow1_p2)
        self.Label1.place(relx=0.1, rely=0.11, height=18, width=86)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Label''')

        self.Message1 = Message(self.TPanedwindow1_p2)
        self.Message1.place(relx=0.1, rely=0.83, relheight=0.11, relwidth=0.84)
        self.Message1.configure(text='''Message''')
        self.Message1.configure(width=83)

        self.Checkbutton3 = Checkbutton(self.TPanedwindow1_p2)
        self.Checkbutton3.place(relx=0.1, rely=0.28, relheight=0.11
                , relwidth=0.63)
        self.Checkbutton3.configure(activebackground="#d9d9d9")
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='''Check''')
        self.Checkbutton3.configure(variable=firstgui_support.che44)

        self.Checkbutton4 = Checkbutton(self.TPanedwindow1_p2)
        self.Checkbutton4.place(relx=0.1, rely=0.39, relheight=0.11
                , relwidth=0.63)
        self.Checkbutton4.configure(activebackground="#d9d9d9")
        self.Checkbutton4.configure(justify=LEFT)
        self.Checkbutton4.configure(text='''Check''')
        self.Checkbutton4.configure(variable=firstgui_support.che45)

        self.Spinbox1 = Spinbox(self.TPanedwindow1_p2, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.1, rely=0.67, relheight=0.14, relwidth=0.81)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(font=font9)
        self.Spinbox1.configure(from_="1.0")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(textvariable=firstgui_support.spinbox)
        self.Spinbox1.configure(to="100.0")

        self.Radiobutton3 = Radiobutton(self.TPanedwindow1_p2)
        self.Radiobutton3.place(relx=0.1, rely=0.5, relheight=0.11
                , relwidth=0.62)
        self.Radiobutton3.configure(activebackground="#d9d9d9")
        self.Radiobutton3.configure(justify=LEFT)
        self.Radiobutton3.configure(text='''Radio''')

        self.Canvas1 = Canvas(self.PNotebook1_t1)
        self.Canvas1.place(relx=0.02, rely=0.04, relheight=0.92, relwidth=0.97)
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief=GROOVE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=561)

        self.TPanedwindow2 = ttk.Panedwindow(self.Canvas1, orient="vertical")
        self.TPanedwindow2.place(relx=0.02, rely=0.04, relheight=0.91
                , relwidth=0.43)
        self.TPanedwindow2.configure(width=200)
        self.TPanedwindow2_p1 = ttk.Labelframe(height=75, text='Pane 1')
        self.TPanedwindow2.add(self.TPanedwindow2_p1)
        self.TPanedwindow2_p2 = ttk.Labelframe(text='Pane 2')
        self.TPanedwindow2.add(self.TPanedwindow2_p2)
        self.__funcid1 = self.TPanedwindow2.bind('<Map>', self.__adjust_sash1)

        self.Entry2 = Entry(self.Canvas1)
        self.Entry2.place(relx=0.5, rely=0.04,height=25, relwidth=0.37)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(selectbackground="#c4c4c4")

        self.Entry3 = Entry(self.Canvas1)
        self.Entry3.place(relx=0.5, rely=0.22,height=25, relwidth=0.37)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(selectbackground="#c4c4c4")

        self.Button2 = Button(self.Canvas1)
        self.Button2.place(relx=0.48, rely=0.82, height=26, width=67)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(text='''Button''')

        self.Button3 = Button(self.Canvas1)
        self.Button3.place(relx=0.61, rely=0.82, height=26, width=67)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(text='''Button''')

        self.Button4 = Button(self.Canvas1)
        self.Button4.place(relx=0.73, rely=0.82, height=26, width=67)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(text='''Button''')

        self.Button5 = Button(self.Canvas1)
        self.Button5.place(relx=0.86, rely=0.82, height=26, width=67)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(text='''Button''')

        self.Listbox1 = Listbox(self.Canvas1)
        self.Listbox1.place(relx=0.5, rely=0.39, relheight=0.36, relwidth=0.47)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(font=font10)
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(width=264)

        self.Checkbutton1 = Checkbutton(self.Canvas1)
        self.Checkbutton1.place(relx=0.87, rely=0.04, relheight=0.09
                , relwidth=0.11)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''Check''')
        self.Checkbutton1.configure(variable=firstgui_support.che66)

        self.Checkbutton2 = Checkbutton(self.Canvas1)
        self.Checkbutton2.place(relx=0.87, rely=0.13, relheight=0.09
                , relwidth=0.11)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Check''')
        self.Checkbutton2.configure(variable=firstgui_support.che67)

        self.Radiobutton1 = Radiobutton(self.Canvas1)
        self.Radiobutton1.place(relx=0.87, rely=0.22, relheight=0.09
                , relwidth=0.11)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Radio''')

        self.Radiobutton2 = Radiobutton(self.Canvas1)
        self.Radiobutton2.place(relx=0.87, rely=0.3, relheight=0.09
                , relwidth=0.11)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Radio''')
        self.PNotebook1.bind('<Button-1>', firstgui_support.button_press)
        self.PNotebook1.bind('<ButtonRelease-1>', firstgui_support.button_release)
        self.PNotebook1.bind('<Motion>', firstgui_support.mouse_over)

        self.MProgressbar = ttk.Progressbar(top)
        self.MProgressbar.place(relx=0.02, rely=0.94, relwidth=0.17
                , relheight=0.0, height=19)

        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.file = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.file,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="File")
        self.file.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=firstgui_support.open_file,
                font=font9,
                foreground="#000000",
                label="Open")
        self.file.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Close")
        self.edit = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.edit,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Edit")
        self.tools = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.tools,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Tools")
        self.database = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.database,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Database")
        self.database.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Open")
        self.database.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Close")
        self.database.add_separator(
                background="#d9d9d9")
        self.database.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Config File")
        self.windows = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.windows,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Windows")
        self.help = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.help,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Help")
        self.help.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="About")


        self.OutputDisplay = ScrolledText(top)
        self.OutputDisplay.place(relx=0.03, rely=0.02, relheight=0.28
                , relwidth=0.48)
        self.OutputDisplay.configure(background="black")
        self.OutputDisplay.configure(font=font9)
        self.OutputDisplay.configure(foreground="white")
        self.OutputDisplay.configure(highlightcolor="yellow")
        self.OutputDisplay.configure(insertbackground="blue")
        self.OutputDisplay.configure(insertborderwidth="3")
        self.OutputDisplay.configure(selectbackground="#c4c4c4")
        self.OutputDisplay.configure(selectforeground="red")
        self.OutputDisplay.configure(width=10)
        self.OutputDisplay.configure(wrap=NONE)

        self.ErrorDisplay = ScrolledText(top)
        self.ErrorDisplay.place(relx=0.5, rely=0.02, relheight=0.28
                , relwidth=0.48)
        self.ErrorDisplay.configure(background="black")
        self.ErrorDisplay.configure(font=font9)
        self.ErrorDisplay.configure(foreground="white")
        self.ErrorDisplay.configure(insertbackground="blue")
        self.ErrorDisplay.configure(insertborderwidth="3")
        self.ErrorDisplay.configure(selectbackground="#c4c4c4")
        self.ErrorDisplay.configure(selectforeground="red")
        self.ErrorDisplay.configure(width=10)
        self.ErrorDisplay.configure(wrap=NONE)



    def __adjust_sash0(self, event):
        paned = event.widget
        pos = [446, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid0)
        del self.__funcid0

    def __adjust_sash1(self, event):
        paned = event.widget
        pos = [75, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid1)
        del self.__funcid1




# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


if __name__ == '__main__':
    vp_start_gui()




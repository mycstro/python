# -----------------------------------------------------------------------------
# logarithm.py
# -----------------------------------------------------------------------------
"""
Create a GUI application to compute logarithms using the Tkinter module.
"""
try:
    # This will work in Python 2.7
    import Tkinter
except ImportError:
    # This will work in Python 3.5
    import tkinter as Tkinter

# -----------------------------------------------------------------------------
# Create main window.
# -----------------------------------------------------------------------------
root = Tkinter.Tk()

# Create two text boxes and pack them in.
greeting = Tkinter.Label(text="Hello, world!")
greeting.pack(side='top')

advertisement = Tkinter.Label(text="I am logarithm computing GUI.")
advertisement.pack(side='top')

# Define a function to close the window.
def quit(event=None):
    root.destroy()

# Cause pressing <Esc> to close the window.
root.bind('<Escape>', quit)

# Create a button that will close the window.
button = Tkinter.Button(text="Exit", command=quit)
button.pack(side='bottom', fill='both')

# -----------------------------------------------------------------------------
# Create a frame within the main window.
# -----------------------------------------------------------------------------
# The frame will contain the widgets needed to do a calculation.
# Each widget in "frame" is created with "frame" as its first argument.
frame = Tkinter.Frame(root)
frame.pack(side='top')

# Create a text box that explains the calculation.
invitation = Tkinter.Label(frame, text="The natural logarithm of")
invitation.pack(side='left')

# Define an input variable and add an entry box so the user can change its value.
x = Tkinter.StringVar()
x.set('2.71828')
x_entry = Tkinter.Entry(frame, width=8, textvariable=x)
x_entry.pack(side='left')

# Define an output variable and a function to compute its value.
y = Tkinter.StringVar()

def compute_y(event=None):
    from math import log
    # Get x and y from outside the function.
    global x, y

    # Get the string value of the x StringVar and convert it to a float.
    x_value = float(x.get())

    # Compute the floating point value of y.
    y_value = log(x_value)

    # Convert this to a formatted string, and store it in the y StringVar.
    y.set('%.6f' % y_value)

# Bind an event to the x_entry box: pressing <Enter> will calculate the
# logarithm of whatever number the user has typed.
x_entry.bind('<Return>', compute_y)

# Create a button to perform the calculation and pack it into the frame.
compute = Tkinter.Button(frame, text=' is ', command=compute_y)
compute.pack(side='left')

# Create a text box that displays the value of the y StringVar.
y_label = Tkinter.Label(frame, textvariable=y, width=8)
y_label.pack(side='left')

# -----------------------------------------------------------------------------
# Activate the window.
# -----------------------------------------------------------------------------
root.mainloop()
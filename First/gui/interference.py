# -----------------------------------------------------------------------------
# interference.py
# -----------------------------------------------------------------------------
"""
Author:     Jesse M. Kinder
Created:    2016 Apr 15
Modified:   2016 Apr 15

Description
-----------
Build a GUI wrapper to explore the interference pattern of two waves.
"""
try:
    # This will work in Python 2.7
    import Tkinter
except ImportError:
    # This will work in Python 3.5
    import tkinter as Tkinter

# -----------------------------------------------------------------------------
# To use matplotlib, the author must use the TkAgg backend, or none of this will
# work and a long string of inexplicable error messages will ensue.
# -----------------------------------------------------------------------------
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

# Define a bold font:
BOLD = ('Courier', '24', 'bold')

# Create main application window.
root = Tkinter.Tk()

# Create a text box explaining the application.
greeting = Tkinter.Label(text="Create an Interference Pattern", font=BOLD)
greeting.pack(side='top')

# Create a frame for variable names and entry boxes for their values.
frame = Tkinter.Frame(root)
frame.pack(side='top')

# Variables for the calculation, and default values.
amplitudeA = Tkinter.StringVar()
amplitudeA.set('1.0')
frequencyA = Tkinter.StringVar()
frequencyA.set('1.0')

amplitudeB = Tkinter.StringVar()
amplitudeB.set('1.0')
frequencyB = Tkinter.StringVar()
frequencyB.set('1.0')

deltaPhi = Tkinter.StringVar()
deltaPhi.set('0.0')

# Create text boxes and entry boxes for the variables.
# Use grid geometry manager instead of packing the entries in.
row_counter = 0
aa_text = Tkinter.Label(frame, text='Amplitude of 1st wave:')
aa_text.grid(row=row_counter, column=0)

aa_entry = Tkinter.Entry(frame, width=8, textvariable=amplitudeA)
aa_entry.grid(row=row_counter, column=1)

row_counter += 1
fa_text = Tkinter.Label(frame, text='Frequency of 1st wave:')
fa_text.grid(row=row_counter, column=0)

fa_entry = Tkinter.Entry(frame, width=8, textvariable=frequencyA)
fa_entry.grid(row=row_counter, column=1)

row_counter += 1
ab_text = Tkinter.Label(frame, text='Amplitude of 2nd wave:')
ab_text.grid(row=row_counter, column=0)

ab_entry = Tkinter.Entry(frame, width=8, textvariable=amplitudeB)
ab_entry.grid(row=row_counter, column=1)

row_counter += 1
fb_text = Tkinter.Label(frame, text='Frequency of 2nd wave:')
fb_text.grid(row=row_counter, column=0)

fb_entry = Tkinter.Entry(frame, width=8, textvariable=frequencyB)
fb_entry.grid(row=row_counter, column=1)

row_counter += 1
dp_text = Tkinter.Label(frame, text='Phase Difference:')
dp_text.grid(row=row_counter, column=0)

dp_entry = Tkinter.Entry(frame, width=8, textvariable=deltaPhi)
dp_entry.grid(row=row_counter, column=1)

# Define a function to create the desired plot.
def make_plot(event=None):
    # Get these variables from outside the function, and update them.
    global amplitudeA, frequencyA, amplitudeB, frequencyB, deltaPhi

    # Convert StringVar data to numerical data.
    aa = float(amplitudeA.get())
    fa = float(frequencyA.get())
    ab = float(amplitudeB.get())
    fb = float(frequencyB.get())
    phi = float(deltaPhi.get())

    # Define the range of the plot.
    t_min = -10
    t_max = 10
    dt = 0.01
    t = np.arange(t_min, t_max+dt, dt)

    # Create the two waves and find the combined intensity.
    waveA = aa * np.cos(fa * t)
    waveB = ab * np.cos(fb * t + phi)
    intensity = (waveA + waveB)**2

    # Create the plot.
    plt.figure()
    plt.plot(t, intensity, lw=3)
    plt.title('Interference Pattern')
    plt.xlabel('Time')
    plt.ylabel('Intensity')
    plt.show()


# Add a button to create the plot.
MakePlot = Tkinter.Button(root, command=make_plot, text="Create Plot")
MakePlot.pack(side='bottom', fill='both')

# Allow pressing <Return> to create plot.
root.bind('<Return>', make_plot)

# Allow pressing <Esc> to close the window.
root.bind('<Escape>', root.destroy)

# Activate the window.
root.mainloop()


import tkinter
import sys

class StdRedirector():
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.config(state=tkinter.NORMAL)
        self.text_space.insert("end", string)
        self.text_space.see("end")
        self.text_space.config(state=tkinter.DISABLED)

class CoreGUI():
    def __init__(self, parent):
        text_box1 = tkinter.Text(parent, state=tkinter.DISABLED)
        text_box1.pack()

        text_box2 = tkinter.Text(parent, state=tkinter.DISABLED)
        text_box2.pack()

        sys.stdout = StdRedirector(text_box1)
        sys.stderr = StdRedirector(text_box2)

        output_button = tkinter.Button(parent, text="Output", command=self.main)
        output_button.pack()

    def main(self):
        print("Std Output")
        raise ValueError("Std Error")

root = tkinter.Tk()
CoreGUI(root)
root.mainloop()
try:
    import Tkinter as Tk
except ImportError:
    import tkinter as Tk

class QAGame(Tk.Tk):
    def __init__(self, questions, answers, *args, **kwargs):
        Tk.Tk.__init__(self, *args, **kwargs)
        self.title("Questions and answers game")
        self._setup_gui()
        self._questions = questions[:]
        self._answers = answers
        self._show_next_question()

    def _setup_gui(self):
        self._label_value = Tk.StringVar()
        self._label = Tk.Label(textvariable=self._label_value)
        self._label.pack()
        self._entry_value = Tk.StringVar()
        self._entry = Tk.Entry(textvariable=self._entry_value)
        self._entry.pack()
        self._button = Tk.Button(text="Next", command=self._move_next)
        self._button.pack()

    def _show_next_question(self):
        q = self._questions.pop(0)
        self._label_value.set(str(q))

    def _move_next(self):
        self._read_answer()
        if len(self._questions) > 0:
            self._show_next_question()
            self._entry_value.set("")
        else:
            self.quit()
            self.destroy()

    def _read_answer(self):
        answer = self._entry_value.get()
        self._answers.append(answer)

    def _button_classification_callback(self, args, class_idx):
        self._classification_callback(args, self._classes[class_idx])
        self.classify_next_plot()

if __name__ == "__main__":
    questions = ["How old are you?",
             "What is your name?"]
    answers = []
    root = QAGame(questions, answers)
    root.mainloop()
    for q,a in zip(questions, answers):
        print ("%s\n>>> %s" % (q, a))
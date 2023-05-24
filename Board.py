import tkinter as tk
from tkinter import *
from Controller import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sudoku")
        self.minsize(width=500, height=580)
        self.geometry('530x630+100+50')
        self.configure(background='#87CEEB')

        controller = Controller.instance()

        self.board_frame = BoardFrame(self)
        self.board_frame.grid(row=0, column=0, padx=10, pady=10)

        self.numberBar_frame = NumberBarFrame(self)
        self.numberBar_frame.grid(row=1, column=0, padx=10, pady=10)

class NumberBarFrame(tk.Frame):

    controller = Controller.instance()

    def __init__(self, parent):
        super().__init__(parent)

        self.frame = Frame(self, width=450, height=50)
        self.frame.grid(row=1, column=0, padx=0, pady=0)

        self.number_buttons = []

        for i in range(9):
            number = i+1
            button = Button(self.frame, width=5, height=3, text=str(number), command=lambda num=number: self.on_button_click(num))
            button.grid(row=0, column=i, padx=2, pady=0)
            self.number_buttons.append(button)

    def on_button_click(self, number):
        if self.controller.number_selected == None:
            self.controller.number_selected = number
        else:
            self.controller.number_selected = None

class BoardFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='white')

        self.frame = Frame(self, width=450, height=450)
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        self.sections = []

        for i in range(3):
            row = []
            for j in range(3):
                frame = SectionFrame(self.frame)
                frame.grid(row=i, column=j, padx=0, pady=0)
                row.append(frame)
            self.sections.append(row)

class SectionFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='white')

        self.frame = Frame(self, width=150, height=150, borderwidth=2, relief="solid")
        self.frame.grid(row=0, column=0, padx=0, pady=0)

        self.cells = []

        for i in range(3):
            row = []
            for j in range(3):
                button = CellButton(self.frame)
                button.grid(row=i, column=j, padx=0, pady=0)
                row.append(button)
            self.cells.append(row)
                
#todo make the cells buttons ONLY when a number is selected

class CellButton(tk.Button):

    controller = Controller.instance()

    def __init__(self, parent):
        super().__init__(parent)

        self.frame = Frame(self, width=50, height=50, borderwidth=1, relief="solid")
        self.frame.grid(row=0, column=0, padx=0, pady=0)

        self.cell_text = StringVar()
        self.cell_text.set(' ')

        self.button = Button(self.frame, width=5, height=3, textvariable=self.cell_text)
        self.button.configure(command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        if self.controller.number_selected != None:
            self.cell_text.set(self.controller.number_selected)
        else:
            self.cell_text.set(' ')


if __name__ == "__main__":
    app = App()
    app.mainloop()

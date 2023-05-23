import tkinter as tk
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sudoku")
        self.minsize(width=500, height=580)
        self.geometry('500x580+100+50')
        self.configure(background='#87CEEB')

        self.board_frame = BoardFrame(self)
        self.board_frame.grid(row=0, column=0, padx=10, pady=10)

        self.numberBar_frame = NumberBarFrame(self)
        self.numberBar_frame.grid(row=1, column=0, padx=10, pady=10)

class NumberBarFrame(tk.Frame):
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
        print("Button", number, "Clicked!")
        


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
                frame = CellFrame(self.frame)
                frame.grid(row=i, column=j, padx=0, pady=0)
                row.append(frame)
            self.cells.append(row)
                
        

class CellFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame = Frame(self, width=50, height=50, borderwidth=1, relief="solid")
        self.frame.grid(row=0, column=0, padx=0, pady=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()

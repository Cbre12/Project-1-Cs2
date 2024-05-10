from GUI_1 import Gui
from tkinter import *

def main():
# This main creates the GUI window. 

    window = Tk()
    window.title("Grade Calculator")
    window.geometry('300x800')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == "__main__":
    main()
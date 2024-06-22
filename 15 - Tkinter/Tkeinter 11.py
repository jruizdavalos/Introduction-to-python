from tkinter import *
import tkinter.messagebox


root=Tk()

#tkinter.messagebox.showinfo("Title", "This is a messagebox")
response= tkinter.messagebox.askquestion("Quiestion 1", "Do you like coffe")

if response=="yes":
    print("Here is a coffe for you")


root.mainloop()
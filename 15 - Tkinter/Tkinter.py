#Tkinter
from tkinter import *
def display():
    data= entry.get()
    print(data)


root = Tk()

root.geometry("800x600")

entry= Entry(root)
entry.pack()

#hello = Label(root, text="Hello world", fg="red", font=("Arial",16))

#hello.pack()

button = Button(root, text="Click Here", command=display)
button.pack()

root.mainloop()
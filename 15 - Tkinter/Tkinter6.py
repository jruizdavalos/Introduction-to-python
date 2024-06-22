from tkinter import *



root = Tk()
frame=  Frame(root, highlightthickness=1, highlightcolor="Black",padx="60", pady="60")
frame.pack()

frame2= Frame(root)
frame2.pack(side=BOTTOM)

button= Button(frame, text="Buttin1")
button2= Button(frame2, text="Buttin2")

button.pack()
button2.pack()


root.geometry("800x600")




root.mainloop()
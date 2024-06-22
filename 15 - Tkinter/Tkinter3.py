from tkinter import *
def selected():
    label.config(text=check_value.get())


root= Tk()

root.geometry("800x600")
check_value= BooleanVar()


checkbutton= Checkbutton(root, text='Accept Terms', variable=check_value, command=selected)
checkbutton.pack()

#label= Label(root)
#label.pack()

root.mainloop()
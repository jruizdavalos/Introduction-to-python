from tkinter import *
def selected ():
    sugar = sugar_var.get()
    ice = ice_var.get()
    cream = cream_var.get()

    if sugar:
        sugar='Sugar '
    else :
        sugar='No sugar '

    if ice:
        ice='ice '
    else :
        ice='No ice '
    if cream:
        cream='cream '
    else :
        cream='No cream '

    label.config(text="Options selected are: "+ "\n"+sugar+"\n" + ice+"\n" + cream)


root= Tk()

root.geometry("800x600")

sugar_var= BooleanVar()
ice_var= BooleanVar()
cream_var= BooleanVar()


sugar_checkBox =  Checkbutton(root,text="Sugar",variable=sugar_var, command=selected)
ice_checkBox =  Checkbutton(root,text="Ice",variable=ice_var, command=selected)
cream_checkBox =  Checkbutton(root,text="Cream",variable=cream_var, command=selected)


sugar_checkBox.pack()
ice_checkBox.pack()
cream_checkBox.pack()

label= Label(root)
label.pack()


root.mainloop()
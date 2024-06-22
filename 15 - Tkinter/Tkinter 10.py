from tkinter import *


def function1():
    print('Menu item clickeado')

root= Tk()

myMenu= Menu(root)

root.config(menu= myMenu)
submenu= Menu(myMenu)

myMenu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Project')
submenu.add_command(label='Save',command=function1)


status = Label(root,text='This is th current status', bd=1,relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

toolBar= Frame(root, bg='green')
insertButton = Button(toolBar, text='Insert File',command= function1)
deleteButton = Button(toolBar, text='Delete File',command= function1)

insertButton.pack(side=LEFT, padx=2,pady=3)
deleteButton.pack(side=LEFT, padx=2,pady=3)

toolBar.pack()



root.mainloop()
from tkinter import *

import ast

root = Tk()

i=0

def getNumber(num):
    global i
    display.insert(i, num)
    i+=1

def get_operation(operator):
    global i
    length= len(operator)
    display.insert(i,operator)
    i+=length

def clear_all():
    display.delete(0,END)

def undo():
    entireString= display.get()
    if len(entireString):
        newString= entireString[:-1]
        clear_all()
        display.insert(0,newString)
    else:
        clear_all()
        display.insert(0,"")

def calculate():
    entireString=display.get()
    try:
        node= ast.parse(entireString, mode="eval")
        result= eval(compile(node, '<string>','eval'))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")



display = Entry(root)
display.grid(row=1,columnspan=6)


numbers=[1,2,3,4,5,6,7,8,9]
counter = 0
for x in range(3):
    for y in range(3):

        button_text= numbers[counter]
        button= Button(root, text=button_text, width=6,height=3, command= lambda text=button_text:getNumber(text))
        button.grid(row=x+2,column=y)
        counter+=1


button= Button(root, text="0",width=6, height=3,command= lambda :getNumber(0))
button.grid(row=5, column=1)


count=0
operations= ['+','-','*','/','%','*3.14',"(","**",")","**2"]
for x in range(4):
    for y in range(3):
        if count<len(operations):
            button= Button(root, text=operations[count],width=6, height=3, command= lambda text=operations[count]:get_operation(text))
            button.grid(row=x+2,column=y+3)
            count+=1


Button(root,text="AC", width=6,height=3, command= clear_all).grid(row=5,column=0)
Button(root,text="=", width=6,height=3, command=calculate).grid(row=5,column=2)
Button(root,text="<-",width=6,height=3, command= lambda :undo()).grid(row=5,column=4)


root.mainloop()
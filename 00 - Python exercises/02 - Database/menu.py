from tkinter import *
from tkinter import ttk
from tkinter import messagebox


import psycopg2

def run_query(query, parameters=()):
    dbname1 ="studentdb"
    user1="postgres"
    password1="admin123"
    port1="5432"
    
    conn=psycopg2.connect(dbname=dbname1,user=user1,password=password1,port=port1)
    cur= conn.cursor()
    query_result=None

    try:
        cur.execute(query,parameters)
        if query.lower().startswith("select"):
            query_result=cur.fetchall()
        conn.commit()
        
    except psycopg2.Error as e:
        messagebox.showerror("Database Error",str(e))
    finally:
        cur.close()
        conn.close()
    return query_result

def refresh_treeview():
    for item in tree.get_children():
        tree.delete(item)
    records= run_query("select * from students; ")
    for record in records:
        tree.insert('',END,values=record)

def insert_data():
    query="insert into students(name, address, age, number) values (%s,%s,%s,%s)"
    parameters=(nameEntry.get(),addressEntry.get(),ageEntry.get(),numberEntry.get())
    run_query(query,parameters)
    messagebox.showinfo("Information","Data inserted successfull")
    refresh_treeview()

def delete_data():
    select_item= tree.selection()[0]
    print(select_item)
    student_id= tree.item(select_item)['values'][0]
    query= "delete from students where student_id=%s"
    parameters=(student_id,)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data delete successfull")
    refresh_treeview()


def update_data():
    select_item= tree.selection()[0]
    student_id= tree.item(select_item)['values'][0]
    query= "update students set name=%s, address=%s, age=%s, number=%s where student_id=%s"
    parameters=(nameEntry.get(),addressEntry.get(),ageEntry.get(),numberEntry.get(),student_id)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data update successfull")
    refresh_treeview()

def create_table ():
    query= "create table if not exists students (student_id serial primary key,name text,address text, age int, number text)"
    run_query(query)
    messagebox.showinfo("Information", "Table Created")
    refresh_treeview()

root=Tk()

root.title("Student management system ")

frame= LabelFrame(root, text="Student Data")
frame.grid(row=0,column=0,padx=10,pady=10, sticky="ew")

Label(frame,text="Name: ").grid(row=0,column=0,padx=2,sticky="w")
nameEntry= Entry(frame)
nameEntry.grid(row=0,column=1,pady=2,sticky="ew")

Label(frame,text="Address: ").grid(row=1,column=0,padx=2,sticky="w")
addressEntry= Entry(frame)
addressEntry.grid(row=1,column=1,pady=2,sticky="ew")

Label(frame,text="Age: ").grid(row=2,column=0,padx=2,sticky="w")
ageEntry= Entry(frame)
ageEntry.grid(row=2,column=1,pady=2,sticky="ew")

Label(frame,text="Phone Number: ").grid(row=3,column=0,padx=2,sticky="w")
numberEntry= Entry(frame)
numberEntry.grid(row=3,column=1,pady=2,sticky="ew")


'''
------------- Create Buttons ------------
'''
buttonFrame= Frame(root)
buttonFrame.grid(row=1,column=0,pady=5,sticky="ew")


Button(buttonFrame, text="Create Table", command=create_table).grid(row=0,column=0,padx=5)
Button(buttonFrame, text="Add Data",command=insert_data).grid(row=0,column=1,padx=5)
Button(buttonFrame, text="Update Data",command=update_data).grid(row=0,column=2,padx=5)
Button(buttonFrame, text="Delete Data", command=delete_data).grid(row=0,column=3,padx=5)


tree_frame= Frame(root)
tree_frame.grid(row=2,column=0,padx=2,sticky="nsew")

tree_scroll= Scrollbar(tree_frame)

tree_scroll.pack(side=RIGHT, fill=Y)

tree= ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")

tree.pack()
tree_scroll.config(command=tree.yview)
tree['columns']=("Student_id", "Name","Address","Age","Number")
tree.column("#0",width=0,stretch=NO)
tree.column("Student_id",anchor=CENTER,width=80)
tree.column("Name",anchor=CENTER,width=120)
tree.column("Address",anchor=CENTER,width=120)
tree.column("Age",anchor=CENTER,width=50)
tree.column("Number",anchor=CENTER,width=120)

tree.heading("Student_id",text="ID",anchor=CENTER)
tree.heading("Name",text="Name",anchor=CENTER)
tree.heading("Address",text="Address",anchor=CENTER)
tree.heading("Age",text="Age",anchor=CENTER)
tree.heading("Number",text="Number",anchor=CENTER)

refresh_treeview()


root.mainloop()

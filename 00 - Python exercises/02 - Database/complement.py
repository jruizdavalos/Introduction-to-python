
import psycopg2

dbname1 ="studentdb"
user1="postgres"
password1="admin123"
port1="5432"
'''
'''
try:
    conne=psycopg2.connect(dbname=dbname1,user=user1,password=password1,port=port1)
except:
    print("Error try to conection")

def select_table():
    conn= conne
    cur= conn.cursor()
    cur.execute( 
        "select * from students")
    
    print("Select data")
    persona= cur.fetchone()
    while persona:
        print(persona)
        persona= cur.fetchone()
    '''
    personas= cur.fetchall()
    for persona in personas:
        print(persona)

    '''


    conn.commit()
    conn.close()

def create_table(): 

    conn= conne
    cur= conn.cursor()
    
    cur.execute(
        "create table students (student_id serial primary key,name text,address text, age int, number text)"
        )
    print("Student table create")
    conn.commit()
    conn.close()

def insert_data():
    #code to accept data from the user
    name= input("Enter name: ")
    address= input("Enter address: ")
    age= input("Enter age: ")
    number= input("Enter number: ")

    conn= conne
    cur= conn.cursor()
    cur.execute(
        "insert into students(name, address, age, number) values (%s,%s,%s,%s)",(name,address,age,number)
        )
    print("Data added in student table")
    conn.commit()
    conn.close()

def update_data():
    student_id=input("Enter id of the student to be update: ")
    conn= conne
    cur= conn.cursor()
    fields= {
        "1":("name","Enter the new name: "),
        "2":("address", "Enter the new address: "),
        "3":("age","Enter the new age: "),
        "4":("number","Enter the new number")
    }
    print("Which fiel would you like to update: ")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    fieldChoice= input("Enter the number of the field you want to update: ")
    if fieldChoice in fields:
        fieldName, promt= fields[fieldChoice]
        newValue= input(promt)
        sql=f"update students set {fieldName}=%s where student_id= %s"
        cur.execute(
            sql,(newValue,student_id)
        )
        print(f"{fieldName} Update successfully")
    else:
        print("Invalid choice")

    conn.commit()
    conn.close()



def delete_data():
    student_id= input("Enter the ID of the student you want to delete: ")
    conn= conne
    cur= conn.cursor()

    cur.execute("select *from students where student_id= %s",(student_id))
    student= cur.fetchone()
    if student:
        print(f"Student to be deleted: ID {student[0]}, Name:{student[1]}, Address: {student[2]}, Age: {student[3]}, Number: {student[4]}")
        choice=input("Are you sure you want to delete the student? (yes/no) \n")
        if choice.lower()=="yes":
            cur.execute("delete from students where student_id = %s", (student_id,))
            print("Student record deleted ")
        else:
            print("Deletion cancelled")
    else:
        print("Student not found ")


    conn.commit()
    conn.close()

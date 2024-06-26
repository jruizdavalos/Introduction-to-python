import psycopg2
from _tkinter import messagebox


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
        if query.lower().startwich("select"):
            query_result=cur.fechall()
        conn.commit()
        
    except psycopg2.Error as e:
        messagebox.showerror("Database Error",str(e))
    finally:
        cur.close()
        conn.close()
    return query_result


def refresh_treeview():
    records= run_query("select * from students")
    for record in records:
        tree.insert('',END,values=record)
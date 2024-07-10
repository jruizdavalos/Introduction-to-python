from tkinter import *
import bcrypt


def validate(password):
  hash=b'$2b$12$Sh5bKmCVhrrGKLB/eV8xMuPt0hkrnChaDypK0RJY/WT5sh4E9PQbu'
  password= bytes(password, encoding='utf-8')
  if bcrypt.checkpw(password,hash):
    print("Login successful")
  else:
    print("Invalid password")

root= Tk()
root.geometry("400x400")

password_entry=Entry(root)
password_entry.pack()

button= Button(text="Validate", 
              command=lambda: validate(password_entry.get()))

button.pack()

root.mainloop()
from complement import*

from tkinter import*




while True:
  print("\n Welcome to the student database managment system ")
  print("1. Create Table: ")
  print("2. Insert Table: ")
  print("3. Read Table: ")
  print("4. Update Table: ")
  print("5. Delete Table: ")
  print("6. Excit: ")
  choice=int(input("Enter your choice (1-6): "))

  if choice ==1:
    create_table()
  elif choice ==2:
    insert_data()
  elif choice==3:
    select_table()
  elif choice==4:
    update_data()
  elif choice==5:
    delete_data()
  elif choice==6:
    break
  else:
    print("Invalid choice, please enter a valid staments (between 1-6)")
print("Thaks, see you later (-,-)")
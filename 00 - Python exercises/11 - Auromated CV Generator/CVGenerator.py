from tkinter import *

def generate_cv_pdf():
  name= entry_name.get()
  email= entry_email.get()
  phone= entry_phone.get()
  address= entry_address.get()
  wwbsite= entry_website.get()
  skills= entry_skills.get("1.0",END).strip().split('\n')
  work_experience= []
  education =[]

  work_experience_lines= entry_experience.get("1.0",END).strip().split('\n')
  for line in work_experience_lines:
    title,description = line.split(":")
    work_experience.append({'title':title.strip(), 'descriprion':description.strip()})

  education_lines = entry_education.get("1.0",END).strip().split('\n')
  for line in education_lines:
    degree, university= line.split(":")
    education.append({'education':degree.split(),'university': university.split()})


  print(work_experience)
  print(education)
window= Tk()
window.title("CV Generator")


label_name= Label(window, text="Name: ")
label_name.pack()
entry_name = Entry(window)
entry_name.pack()

label_email= Label(window, text="email: ")
label_email.pack()
entry_email = Entry(window)
entry_email.pack()

label_phone= Label(window, text="phone: ")
label_phone.pack()
entry_phone = Entry(window)
entry_phone.pack()

label_address= Label(window, text="address: ")
label_address.pack()
entry_address = Entry(window)
entry_address.pack()

label_website= Label(window, text="website: ")
label_website.pack()
entry_website = Entry(window)
entry_website.pack()

label_skills= Label(window, text="Skills(Enter one skill per line: )")
label_skills.pack()
entry_skills = Text(window,height=5)
entry_skills.pack()

label_education= Label(window, text="Education(One per line in format 'Degree': 'University') ")
label_education.pack()
entry_education = Text(window,height=5)
entry_education.pack()

label_experience= Label(window, text="Experince(Enter one per line in format 'Job Title': 'Description') ")
label_experience.pack()
entry_experience = Text(window,height=5)
entry_experience.pack()

label_about_me= Label(window, text="About me ")
label_about_me.pack()
entry_about_me = Text(window,height=5)
entry_about_me.pack()

button_generate = Button(window, text= "Generate CV", command=generate_cv_pdf)
button_generate.pack()


window.mainloop()

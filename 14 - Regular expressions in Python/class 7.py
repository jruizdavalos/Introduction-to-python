import re

text= "Please contact me at +1 (123) 456-7890 or via email at jhon@example.com"
# +1(123) 456-7890

pattern=r'\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}'
matches=re.findall(pattern,text)
print(matches)
# jhon@example.com
pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Za-z]{2,}\b"
matches=re.findall(pattern,text)


print(matches)

#Validation email
email= input("Enter email address")
if re.match(pattern,email):
    print("Valid email")
else:
    print("Invalid email")
import re

text="The variable name is my_var123! \n"
pattern=r"\W"
matches= re.findall(pattern,text)

print(matches)

text1="The sentence \t includes punctuations! \n"
pattern1=r"\s"
matches1= re.findall(pattern1,text1)

print(matches1)
pattern1=r"\S"
matches1= re.findall(pattern1,text1)

print(matches1)

pattern1=r"\S+"
matches1= re.findall(pattern1,text1)

print(matches1)
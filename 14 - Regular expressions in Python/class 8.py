import re

text= "Date: 2023-06-08"
pattern= r"\d{4}-\d{2}-\d{2}"

dates= re.findall(pattern,text)

print(dates)
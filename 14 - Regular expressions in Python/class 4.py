import re

text="the sun ins shining, the birds are singing"
pattern=r"the"

matches=re.findall(pattern,text)
print(matches)


text1="The cat and the dog sat on the mat"
pattern1=r"[abc]"
matches1=re.findall(pattern1,text1)
print(matches1)

text2="The meeting is schedule at 9 34 43 55 6 AM"
pattern2=r"\d"
pattern3=r"\D"
matches2=re.findall(pattern2,text2)
matches3=re.findall(pattern3,text2)
print(matches3)
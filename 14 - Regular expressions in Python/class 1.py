import re

#print(r"Hellos \n world"

string="bca"
pattern="a"
if re.match(pattern,string):
    print('Match found')

else:
    print('No match found')

if re.search(pattern,string):
    print('Match found')

else:
    print('No match found')

stringw="abca"
patternw="ab*c"
if re.match(patternw,stringw):
    print('Match found')

else:
    print('No match found')

string3="aaaaaaaabc"
pattern3=r"a+bc"

if re.match(pattern3,string3):
    print('Match found')

else:
    print('No match found')
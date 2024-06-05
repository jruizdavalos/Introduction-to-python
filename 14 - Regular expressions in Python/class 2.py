import re

string="abbc"
pattern=r"ab{2}c"

if re.match(pattern,string):
    print("Match found")
else:
    print("No match found")

string1="aasdasddb"
pattern1=r"a.b"
if re.match(pattern,string):
    print("Match found")
else:
    print("No match found")

string2 = "bc"
pattern2 = r"a?bc"
if re.match(pattern2, string2):
    print("Match found")
else:
    print("No match found")

string3 = "pythonfile"
pattern3 = r"python-?file"
if re.match(pattern3, string3):
    print("Match found")
else:
    print("No match found")

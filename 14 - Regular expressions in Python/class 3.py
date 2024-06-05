import re


string2 = "91878988888898"
pattern2 = r"^91"
if re.match(pattern2, string2):
    print("Match found")
else:
    print("No match found")

string = "Python"
pattern = r"[aA-z]ython"
if re.match(pattern, string):
    print("Match found")
else:
    print("No match found")

string3 = "abcdABCD"
pattern3 = r"[aA-zZ]"
if re.match(pattern3, string3):
    print("Match found")
else:
    print("No match found")
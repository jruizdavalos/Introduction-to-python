import re

text="Helloooooo, Python is awesomeeeee!"

pattern=r"\w*o+\w*"
#\w*:Matches zero or more alphanumeric characters
#0+:Matches one or more ocurrences of the letter 'o'
#\w*: Matches zero or more alphanumeric characters
matches=re.findall(pattern,text)

print(matches)

#o
#ao
#aoo
#aoooob
#ooooob

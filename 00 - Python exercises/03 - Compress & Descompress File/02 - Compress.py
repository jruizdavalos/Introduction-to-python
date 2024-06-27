from gtts import gTTS
import os

text= open('demo2.txt','r').read()

language='en'

output= gTTS(text=text,lang=language,slow=False)
output.save('fileouput.mp3')

os.system('start fileouput.mp3')

from gtts import gTTS
import os

text= "LOL this is really funny"
text1= "Buen dia"

output= gTTS(text=text1, lang='en', slow=False)

output.save('output.mp3')

os.system("start output.mp3")

#Write

#file= open('data.txt','w')
#delete all
#file.write('New content to be added to file')

#Add information 
file= open('data.txt','a')
content='\nThis is a third line'
file.write(content)
file.close()
#File handling


file= open('data.txt','r')
content1= file.readline()
file.close()

print(content1)
file= open('data.txt','r')
content2=file.read()
print(content2)
file.close()
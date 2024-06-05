with open('data.txt','r') as file:
    contents = file.read()
    print(contents)

with open('data.txt','r') as file:
    line1 = file.readline()
    line2= file.readline()

print(f"\n\t line 1--- {line1}")
print(f"\n\n {line2}")

with open('data.txt','r') as file:
    lines= file.readlines()

print(lines)
for line in lines:
    print(line.strip())

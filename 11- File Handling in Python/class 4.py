while True:
    with open('names.txt','a') as file:
        name = input("Enter name to be added: ")
        file.write(name+"\n")
        choice = input("Do you want add more names? (y/n): ")
        if choice=='n':
            break

with open("names.txt",'r') as file:
    lines= file.readlines()

for line in lines:
    print(line.strip().capitalize())
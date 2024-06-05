'''

counter=0

while counter <=10:
    print(counter)
    if counter ==5:
        print("break in 5")
        break
    counter+=1
print("line after the loop")


'''

counter=0

while counter <=10:

    counter=counter+1
    if counter ==5:
        continue
    print(counter)

print("line after the loop ")
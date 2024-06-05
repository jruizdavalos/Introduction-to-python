'''

Coding challenge part 2.

Create a list of your favourite food items, the list should have minimum 5 elements.

List out the 3rd element in the list.

Add additional item to the current list and display the list.

Insert an element named tacos at the 3rd index position of the list and print out the list elements.

For solution refer next lecture

'''

foods= ['pizza','pasta','burger','hot dog','milanesa']

print(foods[2])
foods.append('fish')
print(foods)

foods.insert(3,'tacos')

print(foods)
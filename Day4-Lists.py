states = ["Delaware", "Florida", "Alabama", "California"] #this allows you to make many variables into one

print(states[0])#this would print the first item in the list "states"

# states[2] #new variable relating to Alabama
print(states[-1]) #prints the last item in the variable

#editing the item specific, will be changed in the list
states[2] = "Bama"
print(states)

#append - adds item to end of list
states.append("Arizona")
print(states)

#extends the list
states.extend(["Ohio", "New Mexico"])
print(states)

num_of_states = len(states) #taking total number of items in the states variable
print(states[num_of_states - 1]) #prints the list, but findind the last entry by taking 1 less than the total number of items (beacuse first entry is 0)

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
veggies = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, veggies] #nested list
print(dirty_dozen[0][1]) #first number checks for the list, second number checks for the item
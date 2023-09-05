# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_items = len(names) #Get total number of items in list; len() counts the number of items in the list

random_choice = random.randint(0, num_items-1) #range from the first position to the last; remember the first position starts with 0, so last position will be 1 less
person_paying = names[random_choice] #takes the random_choice function and applies it to the names

print(f"{person_paying} is going to buy the meal today!")

### Option 2 ###

# person_paying = random.choice(names)

# print(f"{person_paying} is going to buy the meal today!")
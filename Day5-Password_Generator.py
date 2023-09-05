#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
 #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
# nr_letters = 4

for letter in range (1, nr_letters + 1): #1 - 4, not inclusive so have to put + 1
    password += random.choice(letters) #randomly chooses n letter(s) from letters list and adds to password    

for symbol in range (1, nr_symbols + 1):
    password += random.choice(symbols) #randomly chooses n symbol(s) from symbols list and adds to password
    
for number in range (1, nr_numbers + 1):
    password += random.choice(numbers) #randomly chooses n number(s) from numbers list and adds to password
        
print(f"Here is your new password: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

# nr_letters = 4
for letter in range (1, nr_letters + 1): #1 - 4, not inclusive so have to put + 1
    password_list.append(random.choice(letters)) #randomly chooses n letter(s) from letters list and adds to password; adds to end of the password list
    # print(random_letter)    

for symbol in range (1, nr_symbols + 1):
    password_list.append(random.choice(symbols)) #randomly chooses n symbol(s) from symbols list and adds to password; adds to end of the password list
    # print(random_symbol)

for number in range (1, nr_numbers + 1):
    password_list.append(random.choice(numbers)) #randomly chooses n number(s) from numbers list and adds to password; adds to end of the password list
    # print(random_number)    
# new list created above should now have numbers, letters and symbols

random.shuffle(password_list) #shuffles the contents of the new list created
password = "" #now creating a new password back as a string
for char in password_list:
    password += char #adding the randomly shuffled characters from the list to the new password string
print(f"Here is your new password: {password}")
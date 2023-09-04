# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print("Not leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not leap year.")

### Option 2 ###

if year % 4 == 0: #when there is no remainder from leap year / 4
    if year % 100 == 0: #no remainder from leap year / 100
        if year % 400 == 0: #no remainder from leap year / 400
            print("Leap year.") #true for all 3 conditions
        else:
            print("Not leap year.") #meets condition 1 and 2, doesn't mean the 3rd condition
    else:
        print("Leap year.") #meets conditions 1, not 2
else:
    print ("Not leap year.") #does not meet condition 1

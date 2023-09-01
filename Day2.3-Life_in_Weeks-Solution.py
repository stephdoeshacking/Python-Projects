# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)

eol = 90
years_remaining = eol - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12



print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")


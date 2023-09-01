#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to splint the bill? "))

tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = total_tip + bill
per_person = total_bill / people
final_amount = round(per_person, 2)
final_amount = "{:.2f}".format(per_person)

end = str(f"Each person should pay: ${final_amount}")

print(end)

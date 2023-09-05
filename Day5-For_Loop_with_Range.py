# For loop with range
for number in range (1,11): #have to do 11 because it is not inclusive
    print(number)

for number in range (1,11,2): #range starting at 1, goes to 10, skips by 2s
    print(number)

total = 0
for number in range(1,101):
    total += number # could use total = total + number
print(total)
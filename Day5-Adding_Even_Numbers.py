even_range = range(2,101,2)

# for even in even_range: #101 to include 100, start at 2 to not even bother with the one, makes getting even numbers easier
#     print(even)
    
total = 0
for number in even_range:
    total += number
print(total)


### Option 2 ###
# total2 = 0
# for number in range(1,101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)
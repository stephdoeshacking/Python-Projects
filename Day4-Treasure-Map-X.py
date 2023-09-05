# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"] #list for row 1
row2 = ["⬜️","⬜️","️⬜️"] #list for row 2
row3 = ["⬜️️","⬜️️","⬜️️"] #list for row 3
map = [row1, row2, row3] #nested list, spits out the map
print(f"{row1}\n{row2}\n{row3}") #prints above lists, creating map
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# if position == "11":
#     row1[0] = "X" #place x in row 1 first sqaure
# elif position == "12":
#     row1[1] = "X"
# elif position == "13":
#     row1[2] = "X"
# elif position == "21":
#     row2[0] = "X"
# elif position == "22":
#     row2[1] = "X"
# elif position == "23":
#     row2[2] = "X"
# elif position == "31":
#     row3[0] = "X"
# elif position == "32":
#     row3[1] = "X"
# elif position == "33":
#     row3[2] = "X"
# else:
#     print("X")


## Using lists ## 
# input from position will be a string: ex) "23" - string & 0 position is 2 and 1 position is 3
treasure_column = int(position[0]) #first digit; must change str to int
treasure_row = int(position[1]) #second digit; must change str to int

selected_row = map[treasure_row-1]
selected_row[treasure_column-1] = "X"

    

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}") #prints new map after treasure has been set


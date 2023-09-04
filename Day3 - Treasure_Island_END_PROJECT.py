print('''

       _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("There are two caves. Do go left or right?")

if direction == "left" or direction =="Left":
    swim = input("You have run into a large underground lake with a house across the way, do you swim or take the janky canoe?")
    
    if swim == "janky canoe" or swim == "canoe":
        door = input("You have reached the house. There are three colored doors. Which color door do you choose: Red, White, or Blue?")
        
        if door == "White" or door == "white":
            print("You Win!")
        elif door == "Red" or door == "red":
            print("Burned by fire. Game Over.")
        elif door == "Blue" or door =="blue":
            print("Eaten by beats. Game Over.")

    else:
        print("Attacked by trout. Game Over.")           
else:
    print("Fall into a hole. Game over")


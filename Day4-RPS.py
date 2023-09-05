import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock, paper, scissors] #calling images
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")) #taking the user's choice, turning into an integer
computer = random.randint(0, 2) #computer's random choice

print(f"You chose: \n {options[user]} \n Computer chose: \n {options[computer]}") #printing the image that corresponds with the user and computer's choices

if user >= 3 or user < 0:
    print("You typed an invalid number, you lose!")
elif user == 0 and computer == 2:
    print("You win!")
elif computer > user:
    print("You lose!")
elif computer == user:
    print("It's a draw!")
elif computer == 0 and user == 2:
    print("You lose!")
elif computer < user:
    print("You win!") 
elif user >= 3 or user < 0:
    print("You typed an invalid number, you lose!")
   
#################### Steven's ###########################

# #Creates list for game options
# game_options= ["Rock", "Paper", "Scissors"]

# ####Player Options
# player_decision = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")

# if player_decision != "0" and player_decision != "1" and player_decision != "2":
#     print("You entered an invalid option. You lose.")

# else:
#     #Takes user input and converts it to an integer. The integer is then used to select the index from the list.
#     player_selection = game_options[int(player_decision)]

#     if player_selection == "Rock":
#         print(f"Player\n{rock}")

#     elif player_selection == "Paper":
#         print(f"Player\n{paper}")

#     else:
#         print(f"Player\n{scissors}")

#     ####CPU Options
#     cpu_decision = random.randint(0, 2)

#     cpu_selection = game_options[int(cpu_decision)]

#     if cpu_selection == "Rock":
#         print(f"Computer\n{rock}")

#     elif cpu_selection == "Paper":
#         print(f"Computer\n{paper}")

#     else:
#         print(f"Computer\n{scissors}")


#     ####Win or Lose Decision

#     if player_selection != cpu_selection:
#         if player_selection == "Rock" and cpu_selection == "Scissors":
#             print("You Win!")

#         elif player_selection == "Scissors" and cpu_selection == "Paper":
#             print("You Win!")

#         elif player_selection == "Paper" and cpu_selection == "Rock":
#             print("You Win!")

#         elif player_selection == "Rock" and cpu_selection == "Paper":
#             print("You lose.")

#         elif player_selection == "Scissors" and cpu_selection == "Rock":
#             print("You lose.")

#         elif player_selection == "Paper" and cpu_selection == "Scissors":
#             print("You lose.")

#     else:
#         print("It's a Draw.")
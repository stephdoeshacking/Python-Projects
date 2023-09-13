#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
display = []
#For each letter in the chosen_word, add a "_" to 'display'. So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for _ in range(len(chosen_word)):
    display += "_"
print(display)

#

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(len(chosen_word)): #now we are checking the position of the letter within the chosen random word
    letter = chosen_word[position] #letter now going to be matching the position
    if letter == guess:
        display[position] = letter #taking the display list with the correct position from the word and replacing the _ with the correct letter
    

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
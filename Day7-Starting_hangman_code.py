#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list) #variable for picking a random word from the aboce list

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. = .lower()
guess = input("Guess a letter: ").lower() #variable for the letter the user decides, taking any input and making it lowercase

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word: #saying that for 'letter' that in the randomly chosen word from the list:
    if letter == guess: #if the letter is in the word and matches the user's guess, print they are correct
        print("Correct")
    else: #if the letter and guess are not equal, print they are wrong
        print("Wrong")



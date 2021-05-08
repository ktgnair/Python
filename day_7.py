# Hangman's Game
# Step 1: Picking a random word and checking the answers
# ToDo 1: Randomly choose a word from the word_list and assign it to a variable called chosen_word. 
# ToDo 2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# ToDo 3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

word_list = ["handsome", "book", "baseball", "cringe", "teammate"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(f"The chosen word is - {chosen_word}")

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter?\n").lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if guess == letter:
        print("Right choice")
    else:
        print("Wrong Choice")
# Hangman's Game
# Step 3: Checking if the player has won
# ToDo 1: Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

import random

word_list = ["handsome", "book", "baseball", "cringe", "teammate"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(f"The Hint is - {chosen_word}")
word_length = len(chosen_word)

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display.append("_")

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.
stop_game = False
while not stop_game :
    guess = input("Guess a letter?").lower()

# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess

    print(display)
    if "_" not in display:
        stop_game = True
        print("You have won")
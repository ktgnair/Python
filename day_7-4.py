# Hangman's Game
# Step 4: Improving the User Experience.
# ToDo 1: Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["handsome", "book", "baseball", "cringe", "teammate"] 
# ToDo 2: Import the stages from hangman_art.py.
# ToDo 3: Import the logo from hangman_art.py and print it at the start of the game.
# ToDo 4: If the user has entered a letter they've already guessed, print the letter and let them know.
# ToDo 5: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

import random
from hangman_art import logo, stages
from hangman_words import word_list

# Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
list_to_string = " "

print(f"The Hint is - {chosen_word}")

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

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("You have already guessed this letter")

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess

    # If guess is not a letter in the chosen_word,Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The entered letter {guess} is not present in the word")
        lives -= 1
        print(f"You have {lives} chances remaining")
        
        if lives == 0:
            stop_game = True
            print("You Lost the game")

    # To convert the output from list to string using join()
    # Alternative way  - print(f"So far you have finished - {' '.join(display)}")  
    print(list_to_string.join(display))

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    # Import the stages from hangman_art.py.
    print(stages[lives])
    
    if "_" not in display:
        stop_game = True
        print("You have won")
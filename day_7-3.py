# Hangman's Game
# Step 4: Keeping Track of Player's Lives.
# ToDo 1: Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6. 
# ToDo 2: If guess is not a letter in the chosen_word,Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."
# ToDo 3: Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

import random

word_list = ["handsome", "book", "baseball", "cringe", "teammate"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''']

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# print(f"The Hint is - {chosen_word}")
word_length = len(chosen_word)
lives = 6
list_to_string = " "

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

    # If guess is not a letter in the chosen_word,Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(f"You have got {lives} chances")
        # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
        print(stages[lives])
        if lives == 0:
            stop_game = True
            print("You Lose")

    # To convert the output from list to string using join()  
    print(list_to_string.join(display))
    # Alternative way  - print(f"So far you have finished - {' '.join(display)}")
    
    if "_" not in display:
        stop_game = True
        print("You have won")
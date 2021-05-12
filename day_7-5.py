# Hangman's Game - Complete Code

import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

# Choosing a random word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Creating an empty List called display and for each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display.append("_")

stop_game = False
while not stop_game :
    guess = input("Guess a letter?").lower()

    if guess in display:
        print("You have already guessed this letter")

    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess

    if guess not in chosen_word:
        print(f"The entered letter {guess} is not present in the word")
        lives -= 1
        print(f"You have {lives} chances remaining")
        
        if lives == 0:
            stop_game = True
            print("You Lost the game")

    # To convert the output from list to string using join()  
    print(" ".join(display))
    print(stages[lives])
    
    if "_" not in display:
        stop_game = True
        print("You have won")
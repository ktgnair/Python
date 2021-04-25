# Rock Paper Scissors Game

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
game_elements = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if (user_choice >= 3) or (user_choice < 0): 
    print("Please enter a valid input out of these three - 0 for Rock, 1 for Paper or 2 for Scissors. ")
else:
    print(f"You chose: {game_elements[user_choice]}")

    computer_choice = random.randint(0,2)
    print(f"Computer chose: {game_elements[computer_choice]}")

# Way 1 to write the conditions
    # if ((user_choice == 0) and (user_choice == 2)) or ((user_choice == 2) and (user_choice == 1)) or ((user_choice == 1) and (computer_choice == 0)):
    #     print("You Win!!!")
    # elif user_choice == computer_choice :
    #     print("The game is Draw")
    # else:
    #     print("Sorry You Lost the game")

# Way 2 to write the conditions(but little more understandable)
    if ((user_choice == 0) and (computer_choice == 2)):
        print("You Win!!!")
    elif ((computer_choice == 0) and  (user_choice == 2)):
        print("Sorry You Lost the game")
    elif computer_choice > user_choice:
        print("Sorry You Lost the game")
    elif user_choice > computer_choice:
        print("You Win!!!")
    elif user_choice == computer_choice:
        print("The game is Draw")
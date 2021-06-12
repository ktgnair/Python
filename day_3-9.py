#Treasure Island Game

#The below treasure art is taken from "https://ascii.co.uk/art"
#As written the print() starting and ending with (''') means it allows a big string to print 
print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************

''')

print("Welcome to Treasure Island")
print("You are on an hunt for an ancient treasure trove. You cross the dense forest and you reach two caves ")

cave_choice = input("Inside which cave will you go first - Left or Right! \n").lower()

if cave_choice == "right":
  print("You reach a lake. There is a small boat appearing towards you.\n ")
  lake_choice = input("Will you wait for the boat or swim - Wait or Swim \n").lower()

  if lake_choice == "wait":
    print("You reach other side, over there you see three doors\n On which the following symbols are drawn\n Thunder, Snowflake and Circle ")
    door_choice = input("Which door would you choose - Thunder, Snowflake or Circle \n").lower()

    if door_choice == "thunder":
      print("You are struck by a lightning. Game Over!! ")
    elif door_choice == "circle":
      print("You fell into a deep hole. Game Over!! ")
    elif door_choice == "snowflake":
      print("You reached the room which has the treasure. Congrats You Won the Game!!! ")
    else:
      print("Game Over!! ")

  else:
    print("Attacked by some unknown creature in water. Game Over!! ")

else:
  print("The cave enterance is closed by a big rock and you are stuck inside the cave without any air. Game Over!! ")
  
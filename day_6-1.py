# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Hurdle 4

# Hurdles race
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position, the height and the number of hurdles changes each time this world is reloaded.
# What you need to know
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.
# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def front_clear():
    while front_is_clear():
        move()
       
def check_wall():
    while wall_on_right():
        move()
    while not wall_on_right():
        turn_right()
        move()
        turn_right()
        front_clear()
          
def jump():
    turn_left()
    move()
    check_wall()
    turn_left()
    
while not at_goal():   
    if wall_in_front():
        jump()
    else:
        move()
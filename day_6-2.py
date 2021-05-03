# Reeborg's World

# Lost in a maze
# Reeborg was exploring a dark maze and the battery in its flashlight ran out.
# Write a program using an if/elif/else statement so Reeborg can find the exit. 
# The secret is to have Reeborg follow along the right edge of the maze, 
# turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif not wall_on_right():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
        if front_is_clear():
            move()
        else:
            turn_left()
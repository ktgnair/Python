# Area Calculator
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 ✖️ 4) ÷ 5 = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

import math

height_of_wall = int(input("Enter the height of the wall to be painted "))
width_of_wall = int(input("Enter the width of the wall to be painted "))
coverage_per_can = 5

def paint_calc(height, width, coverage):
    number_of_cans = (height_of_wall * width_of_wall) / coverage_per_can
    # Using print(round(number_of_cans)) will give me the output as 1 if input is 2,3,5 but i need 2 as paint cannot be 1.2 can
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint. ")

paint_calc(height=height_of_wall, width=width_of_wall, coverage=coverage_per_can)
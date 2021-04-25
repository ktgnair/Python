# Treasure Map
# Write a program which will mark a spot with an X.

# You need to add a variable called map.This map contains a nested list.
# When map is printed this is what the nested list looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# Format the three rows into a square, like this:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# Write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:23
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']

# For the below image in the list just go to https://emojipedia.org/empty-page/ and copy that emoji and paste it in the code
row1 = ["🗌", "🗌", "🗌"]
row2 = ["🗌", "🗌", "🗌"]
row3 = ["🗌", "🗌", "🗌"]
treasure_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
column_no = int(position[0])
row_no = int(position[1])

treasure_map[row_no - 1][column_no - 1] = "❌"
# print(treasure_map)
print(f"{row1}\n{row2}\n{row3}")
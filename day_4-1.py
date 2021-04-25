# Heads or Tails
# Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# The first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

import random

random_toss = random.randint(0, 1)

if random_toss == 0:
    print("Tails")
else:
    print("Heads")



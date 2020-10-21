import random
import sqlite3

## For database holding points for dice roller

## Dice roller
# !roll

def roll():
    x = random.randrange(6)+1
    print("The dice rolls on {0}...".format(x))
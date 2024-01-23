# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 01:37:52 2024

@author: Dan Nguyen
"""

import random
import matplotlib.pyplot as plt 


game = ["Action", "Puzzle", "RPG", "Rhythm"]
numPlayed = [0, 0, 0, 0]

for i in range(len(game)):
    numPlayed[i] = random.randint(0, 10)
    
colour = ["Red", "Blue", "Green", "Yellow"]
plt.title("Favourite Video Game Genre")
plt.pie(numPlayed, labels = game, autopct = '%2.1f%%', colors = colour)
plt.show()
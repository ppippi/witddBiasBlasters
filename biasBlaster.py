#libraries
#import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
#import os, glob


print("Welcome to Bias Blaster!\n")
charName = raw_input('Name your character: ')
print("Hi %s, let's begin!" % charName)

#level 1
print("Level 1")
time.sleep(1)
print("It's your first day. You're walking down the hallway towards your desk when you pass by...")
time.sleep(3)

imgplot = plt.imshow(mpimg.imread('level1.png'))
plt.ion()
plt.show()
#animal_name = raw_input("What is the name?: ")
plt.close(5)

print("Based on the image displayed, select one of the following terms based on who you think this person is: ")

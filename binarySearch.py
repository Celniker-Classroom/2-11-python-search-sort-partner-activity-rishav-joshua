#write your python code here

#Import statement to use random generation
from random import randint

randNums = []

#Adds a random number 10 times
for i in range(10):
    #Generates a random number, then appends it
    randNums.append(randint(1,50))

randNums.sort()

searched = randint(1.20)


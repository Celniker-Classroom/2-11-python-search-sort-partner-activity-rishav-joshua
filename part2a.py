#write your python code here

#Import statement to use random generation
from random import randint

randNums = []

#Adds a random number 10 times
for i in range(10):
    #Generates a random number, then appends it
    randNums.append(randint(1,50))

searched = randint(1,20)

if searched in randNums:
    print(f"Generated list: {randNums} \n Searching for number: {searched} \n Number {searched} found in the list!")
else:
    print(f"Generated list: {randNums} \n Searching for number: {searched} \n Number {searched} not found in the list!")
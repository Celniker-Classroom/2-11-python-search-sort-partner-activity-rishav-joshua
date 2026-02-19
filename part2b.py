#write your python code here

#Import statement to use random generation
from random import randint

randNums = []

#Adds a random number 10 times
for i in range(10):
    #Generates a random number, then appends it
    randNums.append(randint(1,50))

searched = randint(1,20)


comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found



for num in randNums:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if num == searched:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found

if found:
    print(f"Generated list: {randNums} \n Searching for number: {searched} \n Number {searched} found in the list after {comparisons} comparisons!")
else:
    print(f"Generated list: {randNums} \n Searching for number: {searched} \n Number {searched} not found in the list after {comparisons} comparisons!")
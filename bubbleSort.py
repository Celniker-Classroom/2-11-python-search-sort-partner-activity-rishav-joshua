#write your python code here


#Import statement to use random generation
from random import randint


randNums = []


#Adds a random number 13 times
for i in range(13):
    #Generates a random number, then appends it
    randNums.append(randint(1,50))

#Once it's sorted the loop will terminate
sorted = False

#Keeping track of comparisons
comparisons = 0

#Making sure we aren't modifying the original
randCopy = randNums

while not sorted:
    #Assumes sorted every round until it finds a mismatch
    sorted = True
    for i in range(len(randCopy)-1):
        if randCopy[i] > randCopy[i+1]:
            #As long as this if loop runs, at least one thing is not sorted (there's a mismatch) so sorted = False
            sorted = False
            #Switches the out of order elements
            randCopy[i], randCopy[i+1] = [randCopy[i+1], randCopy[i]]
        #Increments comparisons because one comparison has been made
        comparisons += 1

print(f"Generated list: {randNums} \n Sorted list: {randCopy} \n Num. Comparisons: {comparisons}")

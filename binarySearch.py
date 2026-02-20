#write your python code here


#Import statement to use random generation
from random import randint


randNums = []


#Adds a random number 13 times
for i in range(13):
    #Generates a random number, then appends it
    randNums.append(randint(1,50))


#List must be sorted for binary search to work
randNums.sort()


#Random integer to search
searched = randint(1,20)


#Determines what message is shown to the user
found = False


#Keeps track of comparisons
comparisons = 0


#Makes sure we are not modifying the original list
randCopy = randNums


#The while loop is rerun on the list each time it is chopped in half until there are no longer any elements or the desired number has been found
while not found:
    #If the number is not found and the list has been emptied the process will still terminate
    if len(randCopy) == 0:
        break
    #If the searched number is larger than the middle number, we discard the lower half of the list
    if (randCopy[len(randCopy) // 2] < searched):
        randCopy = randCopy[len(randCopy) // 2 + 1:]
    #If the searched number is smaller than the middle number, we discard the upper half of the list
    elif (randCopy[len(randCopy) // 2] > searched):
        randCopy = randCopy[:len(randCopy) // 2]
    #If the searched number equals the middle number, we are done
    else:
        found = True
    #Comparisons increments because we have to have made one comparison each round
    comparisons += 1


#Same code as part 2
if found:
    print(f"Generated list: {randNums} \n Searching for number: {searched} \n Number {searched} found in the list after {comparisons} comparisons!")
else:
    print(f"Generated list: {randNums} \n Searching for number: {searched} \n Number {searched} not found in the list after {comparisons} comparisons!")
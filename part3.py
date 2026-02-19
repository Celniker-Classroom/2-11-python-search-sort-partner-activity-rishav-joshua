#write your python code here

#Import statement to use random generation
from random import randint

randNums = []

#Adds a random number 10 times
for i in range(10):
    #Generates a random number, then appends it
    randNums.append(randint(1,50))


#SECTION 1
searched = int(input("What number would you like to search for? "))

if searched in randNums:
    print(f"Generated list: {randNums} \n Searching for number: {searched} \n Number {searched} found in the list!")
else:
    print(f"Generated list: {randNums} \n Searching for number: {searched} \n Number {searched} not found in the list!")


#SECTION 2
smallest = min(randNums)

#SECTION 3
largest = max(randNums)

#SECTION 4
sum = 0

for num in randNums:
    sum += num

#SECTION 5
randNums.sort()

#SECTION 6

import random
from collections import Counter
from itertools import chain

data = [random.randint(1, 10) for _ in range(20)]
print(f"Original List: {data}")

frequency = Counter(data)
print(f"Item Frequency: {dict(frequency)}")

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = list(chain.from_iterable(nested_list))
print(f"Flattened List: {flattened}")

weighted_sample = random.choices(data, k=5)
print(f"Weighted Sample: {weighted_sample}")
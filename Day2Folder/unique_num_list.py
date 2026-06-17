# generate a unique random number list of 100 elements between 1 - 150

import random
numbers = []
counter = 1
x = 0
for i in range(100):
    numbers.append(random.randint(1,150))

for i in range(len(numbers)):
    x = numbers[counter]
    if x in numbers == True:
       while x in numbers:
           numbers.remove(x)
           if x not in numbers:
               break


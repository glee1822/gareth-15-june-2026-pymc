# generate a unique random number list of 100 elements between 1 - 150

import random
numbers = []

x = 0
for i in range(10):
    numbers.append(random.randint(1,15))

for i in range(len(numbers)):
    x = numbers[i]
    if x in numbers == True:
        while x in numbers:
           numbers.remove(x)
        numbers.append(x)

print(numbers)


# generate a unique random number list of 100 elements between 1 - 150

import random
numbers = []

x = 0
for i in range(10):
    numbers.append(random.randint(1,10))


for i in range(len(numbers)):
    x = numbers[i]

    while x in numbers:
       numbers.remove(x)


print(numbers)


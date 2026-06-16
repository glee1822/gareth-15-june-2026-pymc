# generate a list of 100 random number
# not using existing function, 
# find the maximum, minimum, median and mean of the list.
import random
numbers = []
for i in range(100):
    x = random.randint(1,100)
    numbers.append(x)
for i in range (len(numbers)):
    print(numbers[i])
    if numbers[i] > numbers[i+1]:
        print

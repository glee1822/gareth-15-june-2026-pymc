# generate a list of 100 random number
# not using existing function, 
# find the maximum, minimum, median and mean of the list.
import random
numbers = []
num = 0
for i in range(100):
    x = random.randint(1,100)
    numbers.append(x)

for i in range (len(numbers)):
    print(numbers[i])
    if numbers[i] > num:
        num = numbers[i]
print("the highest number is " + str(num))

for i in range (len(numbers)):
    print(numbers[i])
    if numbers[i] < num:
        num = numbers[i]
print("the highest number is " + str(num))
        


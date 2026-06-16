# generate a list of 100 random number
# not using existing function, 
# find the maximum, minimum, median and mean of the list.
import random
numbers = []
highnum = 0
lownum = 100
for i in range(100):
    x = random.randint(1,100)
    numbers.append(x)

for i in range (len(numbers)):
    print(numbers[i])
    if numbers[i] > highnum:
        highnum = numbers[i]
print("the highest number is " + str(highnum))

for i in range (len(numbers)):
    if numbers[i] < lownum:
        lownum = numbers[i]
print("the lowest number is " + str(lownum))
        


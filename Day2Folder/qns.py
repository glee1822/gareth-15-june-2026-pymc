# generate a list of 100 random number
# not using existing function, 
# find the maximum, minimum, median and mean of the list.
import random
numbers = []
highnum = 0
lownum = 1001
totalnum = 0
avgnum = 0
seqnum = 0
arrangednumbers = []
for i in range(100):
    x = random.randint(1,1000)
    numbers.append(x)

for i in range(len(numbers)):
    print(numbers[i])
    if numbers[i] > highnum:
        highnum = numbers[i]
print("the highest number is " + str(highnum))

for i in range(len(numbers)):
    if numbers[i] < lownum:
        lownum = numbers[i]
print("the lowest number is " + str(lownum))
        
for i in range(len(numbers)):
    totalnum += numbers[i]
print("the total of the numbers is " + str(totalnum))
avgnum = totalnum / len(numbers)
print("the average of the numbers is " + str(avgnum))

for a in range(100):
    for i in range(len(numbers)):
            if numbers[i] < lownum:
                lownum = numbers[i]
    numbers.remove(lownum)
    arrangednumbers.append(lownum)
    lownum = 1000
print(arrangednumbers)
# for a more general approach you need to consider if the arranged number is odd or even



halfway_arrangednumbers = len(arrangednumbers) / 2
if halfway_arrangednumbers%2  != 0:
    median = arrangednumbers.index()









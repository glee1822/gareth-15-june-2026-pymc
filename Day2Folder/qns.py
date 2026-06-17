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
median = 0
length = int(input("how many items"))
range_of_list = int(input("what is the range from 1-"))
for i in range(length):
    x = random.randint(1,range_of_list)
    numbers.append(x)
print(numbers)
for i in range(len(numbers)):
    
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

for a in range(length):
    for i in range(len(numbers)):
            if numbers[i] < lownum:
                lownum = numbers[i]
    numbers.remove(lownum)
    arrangednumbers.append(lownum)
    lownum = range_of_list 
print(f"the rearranged list of numbers in order is {arrangednumbers}")
# for a more general approach you need to consider if the arranged number is odd or even

# .index(element) the element inside is the element in the list
# this will tell you the index number of the element in the list.
# for example my_list = [5,4,3,2,1] 
# my_list.index(4) will give you 1
# to access the element in the list using index number, it will be 
# mylist[2] will give you 3.

halfway_arrangednumbers = len(arrangednumbers) // 2 # this one will give you float 
# to prevent having float there are two ways.
#1. you can use math.floor()
#2. you can use // 
# both are the same but 2 no need to input
# 5//2 will give you 2. Basically it give you the quotient
# 5%2 give the remainders
if halfway_arrangednumbers%2  != 0:
    median = arrangednumbers[halfway_arrangednumbers]
    print(f"the median of the numbers is {median}")
else:
    # it should be for even number 
    # after you divide 2
    # you access the list[number//2] and acces the list[number//2 + 1]
    # add them together and get the average
    median = (arrangednumbers[halfway_arrangednumbers] + arrangednumbers[halfway_arrangednumbers + 1]) / 2
    print(f"the median of the numbers is {median}")



# how would you check that your answer or approach is correct ? 
# one of the ways you could do testing with a smaller set of numbers
# for example, you can do testing with a list of 5 elements and 4 elements to see if it works out correctly 

# seems to have some issue
# the rearranged list of numbers in order is [1, 1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 8, 8, 9, 9, 10, 10]







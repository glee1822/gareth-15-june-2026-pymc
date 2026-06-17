# Write all your codes for Day 3 here.
# COMMENT out the previous task before going on to the next task
print("hello from day3")

########################################################################
# Task 1:
# title = input("title")
# name = input("name")
# command = input("command")
# print(title + " " + name + " commands you to " + command)



########################################################################
# Task 2:
# name = input("name")
# num_pens = str(input("num of pens"))
# print(name + " bought " + num_pens + "pens")



########################################################################
# Task 3:
# x = input("num1")
# y = input("num2")
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)


########################################################################
# Task 4:
# total_type_items = int(input("how many types of items in total are you buying"))
# total_cost_of_all = 0
# for i in range(total_type_items):
#     current_item = "nothing"
#     price_current = 0
#     amount_of_items = 0
#     current_item = input("what is the current item you are buying ")
#     price_current = int(input("what is the price of one of " + current_item))
#     amount_of_items = int(input("how many of " + current_item + " do you want to buy "))
#     total_price_of_current = price_current * amount_of_items
#     print("the total price of" + current_item + "is" + str(total_price_of_current))
#     total_cost_of_all = total_cost_of_all + total_price_of_current
# print("the total will be" + str(total_cost_of_all))    



########################################################################
# Task 5:
# num1 = int(input("num1"))
# num2 = int(input("num2"))
# if num1 > num2:
#     print("num1 is larger than num2")
# elif num1 < num2:
#     print("num1 is not larger than num2")
# else:
#     print("num1 is equal to num2")

########################################################################
# Task 6:
# password = input("what is the password")
# answer = input("what is the password")
# if answer == password:
#     print("correct")
# else:
#     print("wrong")
########################################################################
# Task 7:
# import random
# for i in range(10):
#     x = random.randint(1, 10)
#     print(x)


########################################################################
# Task 8:
# import random

# score=0
# for i in range(10):
#     num1 = random.randint(1,10)
#     num2 = random.randint(1,10)
#     answer = int(input(f"what is " + str(num1) + " + " + str(num2) +" ?"))
#     # answer = int(input(f"what is {num1} + {num2} ?"))
#     if answer == num1 + num2:
#         print("correct")
#         score = score + 1
#     else:
#         print("wrong")
# print("ur score is" + str(score))

########################################################################
# Additional exercises:
# password = input("what is the correct password")
# tries = 3
# for i in range(tries):
#     ur_pass = input("wat is ur password")
#     if ur_pass == password:
#         print("correct")
#         break
#     else:
#         tries -= 1
#         print(f"wrong, u have {tries} more tries")
# if tries == 0:
#     print("u are out of tries, system locked")

import random
number = random.randint(1,100)
tries = 20
# for i in range(tries):
#     answer = int(input("what is your guess"))
#     if answer == number:
#         print("correct")
#         break
#     elif answer > number:
#         print("ur answer is too big")
#         tries -= 1
#         print(f"u have {tries} tries left")
#     elif answer < number:
#         print("ur answer is too small")
#         tries -= 1
#         print(f"u have {tries} tries left")
# if tries == 0:
#     print(f"u lose the answer was {number}")
 #solver for above
start = 1
end = 100
print(f"the number is{number}")
for i in range(tries):
    comp_guess = random.randint(start, end)
    print(comp_guess)
    if comp_guess > number:
        end = comp_guess
        
        tries -= 1
    elif comp_guess < number:
        start = comp_guess
        
        tries -= 1
    else:
        print("the computer got it right")
        break
if tries == 0:
    print("the computer dum")

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
total_type_items = int(input("how many types of items in total are you buying"))
total_cost_of_all = 0
for i in range(total_type_items):
    current_item = "nothing"
    price_current = 0
    amount_of_items = 0
    current_item = input("what is the current item you are buying")
    price_current = int(input("what is the price of one of " + current_item))
    amount_of_items = int(input("how many of " + price_current + "do you want to buy"))
    total_price_of_current = price_current * amount_of_items
    print("the total price of" + current_item + "is" + total_price_of_current)
    total_cost_of_all = total_cost_of_all + total_price_of_current
print("the ")    



########################################################################
# Task 5:



########################################################################
# Task 6:



########################################################################
# Task 7:



########################################################################
# Task 8:



########################################################################
# Additional exercises:
# ==============================================================================
# PYTHON COMPLETE PRACTICE WORKBOOK: 40 QUESTIONS & TASKS
# Topics: Variables to Object-Oriented Programming (Inheritance)
# Difficulty: Too Easy to Too Hard
# ==============================================================================

# ------------------------------------------------------------------------------
# SECTION 1: BASICS, VARIABLES, STRINGS & NUMBERS (Too Easy)
# ------------------------------------------------------------------------------



# TASK 1: Hello World Setup
# Print the phrase "Hello, Pycharm and VS Code!" to the console.
# Write your code below:


# print("Hello, Pycharm and VS Code!")




# TASK 2: Drawing a Shape
# Use 4 separate print statements to draw the following right-angled triangle:
# /|
# / |
# /  |
# /___|
# Write your code below:

# print("/|")
# print("/ |")
# print("/  |")
# print("/___|")



# TASK 3: Variables & Data Types
# Create three variables: one storing your name (string), one storing your age (integer),
# and one storing whether you are a student (boolean). Print all three.
# Write your code below:


# name = "Snahasish Dey"
# age = 26
# is_student = True

# print("Hi! My name is " + name + " and I am " + str(age) + " year old. My Student Status: " + str(is_student))




# TASK 4: Working With Strings (Methods)
# Given the string phrase = "Python Programming", convert it completely to uppercase,
# check if it is all uppercase, and then find the index of the letter "P".
# Write your code below:

# x = "Python Programming"
# newx = x.upper()
# print(newx)
# print(newx.isupper())
# print(newx.index("P"))




# TASK 5: Working With Numbers (Arithmetic)
# Calculate and print the result of: 10 raised to the power of 3, plus 5, divided by 2.
# Write your code below:


# import math

# w = 5
# x = 10
# y = 3
# z = 2

# print(((x.__pow__(y))+w)/z)






# TASK 6: Getting Input From Users
# Ask the user for their favorite color using input(), then print a message saying
# "Your favorite color is [color]".
# Write your code below:

# x =  input("Your favourate colour is ")
# print("Your favorite color is " + x)




# TASK 7: Building a Basic Calculator
# Prompt the user to input two decimal numbers. Add them together and print the absolute result.
# Write your code below:


# X1 = input("Enter your 1st Number: ")
# X2 = input("Enter your 2nd Number: ")
# Result = float(X1) + float(X2)
# print(Result)






# TASK 8: Mad Libs Game
# Create a short story format string with three placeholders: a color, a plural noun, and a celebrity.
# Take these three inputs from the user and populate the story.
# Write your code below:

# color = input("Your favourate color: ")
# nouns = input("Your favourate nouns: ")
# celebrity = input("Your favourate celebrity: ")

# print("My favourate celebrity is :" + celebrity + " and she loves " + nouns + " in " + color + " colour")





# ------------------------------------------------------------------------------
# SECTION 2: COLLECTIONS - LISTS & TUPLES (Easy)
# ------------------------------------------------------------------------------

# TASK 9: Accessing Lists
# Create a list called "friends" containing 5 names. Print the first, third, and last name
# using indexing (including negative indexing for the last item).
# Write your code below:

# friends = ["rafik", "jabbar", "salam", "barkat", "promit"]

# print(friends[0])
# print(friends[3])
# print(friends[4])
# print(friends[-1])




# TASK 10: List Functions
# Take the list [4, 8, 15, 16, 23, 42]. Append the number 50 to the end, insert the number 10
# at index 2, remove the number 15, and then sort the list in descending order.
# Write your code below:



# list = [4, 8, 15, 16, 23, 42]

# list.append(50)
# list.insert(7, 10)
# list.remove(15)
# list.sort(reverse=True)
# print(list)






# TASK 11: Tuples vs Lists
# Create an immutable tuple containing the latitude and longitude coordinates of a place.
# Try to change the first value to see the error, then write a comment explaining why it failed.
# Write your code below:


# coordinates = ("24245:2525", "26526525,5625252", "25252:2525425", "2626:27272")

# # Attempting to append a new value
# coordinates.append("1314126:27267276")  

# # ❌ ERROR: 'tuple' object has no attribute 'append'
# # Explanation: Tuples are immutable in Python, meaning once created, 
# # their elements cannot be added, removed, or modified. 
# # Methods like append(), insert(), or remove() only work with lists, not tuples.










# ------------------------------------------------------------------------------
# SECTION 3: FUNCTIONS & CONTROL FLOW (Medium)
# ------------------------------------------------------------------------------

# TASK 12: Creating a Basic Function
# Write a function called `say_hi` that takes a user's name and age as parameters and
# prints: "Hello [name], you are [age] years old." Call the function.
# Write your code below:

# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")
# def line( name, age):
#     print("Hello " + name + ", you are " + str(age) + " years old.")
# line(name, age)





# TASK 13: Functions with Return Statements
# Write a function `cube(num)` that returns the cube of a number. Store the returned
# value in a variable named `result` and print it.
# Write your code below:

# x = input("Enter the number: ")
# def number(x):
#     Result = int(x) * int(x) * int(x)
#     print("Your cubed numbers result is : " + str(Result) )

# number(x)



# TASK 14: Basic If Statements
# Create a boolean variable `is_raining` and another `is_cold`. Write an if/elif/else structure
# that prints the appropriate clothing advice based on combinations of these conditions.
# Write your code below:



# is_raining = True
# is_cold = False

# if is_raining == True and is_cold == True:
#         print("Bring heavy cloths & a raincoat")
# elif is_raining == True and is_cold == False:
#         print("Bring a raincoat")
# elif is_raining == False and is_cold == True:
#         print("Bring heavy cloths")
# else:
#         print("Wear Normal Cloths dude!")







# TASK 15: If Statements & Comparisons
# Write a function `max_num(num1, num2, num3)` that compares three numbers using 
# comparison operators and returns the largest one without using Python's built-in max().
# Write your code below:


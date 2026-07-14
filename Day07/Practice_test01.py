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
# print(abs(Result))






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
# print(friends[2])
# # print(friends[-1])




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

# a = 3
# b = 5
# c = 9

# if a>b and a>c:
#     print("a is the largest number")
# elif b>a and b>c:
#     print("b is the largest number")
# else:
#     print("c is the largest number")  






# TASK 16: Building a Better Calculator
# Prompt the user for a first number, an operator (+, -, *, /), and a second number.
# Use if/elif/else statements to execute the appropriate math operations. Handle division by zero.
# Write your code below:
# try:
        
#     num1 = input("Enter first number: ")
#     operator = input("Enter operator: ")
#     num2 = input("Enter second number: ")

#     Result = None
#     if operator == "+":
#         Result = float(num1) + float(num2)
#     elif operator == "-":
#         Result = float(num1) - float(num2)
#     elif operator == "*":
#         Result = float(num1) * float(num2)
#     elif operator == "/":
#         if num1 == 0 or num2 == 0 :
#             print("Can't devide by 0")
#         else:
#             Result = float(num1) / float(num2)
#     print("the result is: " + str(Result))
# except ValueError:
#     print("Invalid Entry. Enter Valid number Next time")






# TASK 17: Working with Dictionaries
# Create a dictionary representing a smartphone (brand, model, storage_gb, is_5g).
# Print the model, change the storage capacity, and safely fetch a key called "camera_megapixels" 
# using the .get() method with a default fallback value if it doesn't exist.
# Write your code below:

# smartphone = {
#     "brand": "samsung",
#     "model": "S21",
#     "storage_gb": 128,
#     "is_5g": True,
# }

# print(smartphone["model"])
# smartphone["storage_gb"] = 256
# camera_megapixels = smartphone.get("camera_megapixels", "Not available")
# print(camera_megapixels)





# TASK 18: While Loop Countdown
# Write a while loop that prints the numbers from 5 down to 1, and then prints "Blastoff!".
# Write your code below:

# i = 5
# while i > 0:
#     print(i)
#     i -= 1

# print("Blastoff!")






# TASK 19: For Loop over a List
# Given a list of fruits ['apple', 'banana', 'cherry'], use a for loop to print each fruit in uppercase.
# Write your code below:


# fruits = ['apple', 'banana', 'cherry']

# for a in fruits:
#     print(a.upper())





# TASK 20: Dictionary Basics
# Create a dictionary representing a car with keys: brand, model, and year.
# - Print the model.
# - Change the year to a new value.
# - Safely fetch a key called "color" using .get() with a default value "Unknown".
# Write your code below:
# car = {
#     "brand" : "Honda",
#     "model" : "corrola",
#     "year" : "2020",
# }

# print(car["model"])

# car["year"] = 2022

# print(car["year"])
# print(car.get("color", "Unknown"))



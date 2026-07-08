# #2D loops & nested lists

# number_grid = [
#     [1,2,3,],
#     [4,5,6,],
#     [7,8,9,],
#     [0]
# ]
# print(number_grid[0][0]) #prints the first element of the first list in the 2D list\




# For Nested loops
# number_grid = [
#     [1,2,3,],
#     [4,5,6,],
#     [7,8,9,],
#     [0]
# ]

# for row in number_grid: #for loop that iterates through each list in the 2D list
#     for col in row: #for loop that iterates through each element in the list
#         print(col) #prints each element in the list 






# Build a Translator

# def translate(word):
#     translation = ""
#     for letter in word:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation += "G"
#             else:
#                 translation += "g"
#         else:
#             translation += letter
#     return translation

# print(translate(input("Enter a word: "))) #function call that prints the translated word










# Comments
# This program is cool

# '''
# This is a multi-line comment
# '''

# select the text and press ctrl + / to comment or uncomment the selected text








# Try except block
# try:
#     Value = 10/0

#     number = int(input("Enter a number: ")) #input function takes input from the user and converts it to integer
#     print(number) #prints the number entered by the user    

# except ZeroDivisionError: #catches the ZeroDivisionError exception and assigns it to the variable err
#     print("Invalid input") #prints invalid input if the user enters a non-integer value 

# except ValueError: #catches the ValueError exception and assigns it to the variable err
#     print("Invalid input") #prints invalid input if the user enters a non-integer value 



# try:

#     number = int(input("Enter a number: ")) #input function takes input from the user and converts it to integer
#     print(number) #prints the number entered by the user    

# except ZeroDivisionError as err1: #catches the ZeroDivisionError exception and assigns it to the variable err
#     print(err1) #prints invalid input if the user enters a non-integer value 

# except ValueError as err2: #catches the ValueError exception and assigns it to the variable err
#     print(err2) #prints invalid input if the user enters a non-integer value 



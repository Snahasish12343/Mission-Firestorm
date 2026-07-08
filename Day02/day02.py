# Statements & Comparisons

# def max_num(num1, num2, num3): #function definition
#     if num1 >= num2 and num1 >= num3: #if statement
#         return num1 #return statement
#     elif num2 >= num1 and num2 >= num3: #elif statement
#         return num2 #return statement
#     else: #else statement
#         return num3 #return statement

# print(max_num(3, 4, 5)) #function call






# Building a better calculator

# num1 = float(input("input first number: ")) #input function takes input from the user and converts it to float

# op = input("input operator: ") #input function takes input from the user

# num2 = float(input("input second number: ")) #input function takes input from the user and converts it to float

# if op == "+": #if statement
#     print(num1 + num2) #prints the result of the addition
# elif op == "-": #elif statement
#     print(num1 - num2) #prints the result of the subtraction
# elif op == "*": #elif statement
#     print(num1 * num2) #prints the result of the multiplication
# elif op == "/": #elif statement
#     print(num1 / num2) #prints the result of the division   

# elif op == "**": #elif statement
#     print(num1 ** num2) #prints the result of the exponentiation

# else: #else statement
#     print("Invalid operator") #prints invalid 7operator if the operator is not valid
        






# Dictionaries

# monthConversions = {
#     "jan" : "January",
#     "feb" : "February",
#     "mar" : "March",
#     "apr" : "April", 
#     "may" : "May",
#     "jun" : "June",
#     "jul" : "July",
#     "aug" : "August",
#     "sep" : "September",
#     "oct" : "October",
#     "nov" : "November",
#     "dec" : "December"

# }

# print(monthConversions["nov"]) #prints the value of the key "nov" in the dictionary

# print(monthConversions.get("Den", "Not a valid key")) #prints the value of the key "nov" in the dictionary












# While Loops]

# i = 1
# while i < 10:
#     print(i)
#     i = i + 1
# print ("Done with Loop")




# Building a guessing game

# secret_word = "Elephant"

# guess = ""
# guess_count = 0
# guess_limit = 3

# while guess != secret_word and guess_count < guess_limit:
#     guess = input("Enter your guess: ")
#     guess_count += 1

# if guess == secret_word:
#     print("You guessed it right!")
# else:
#     print("You're out of guesses!")





# secret_word = "Elephant"

# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
    
#     if guess_count < guess_limit:
#         guess = input("Enter your guess: ")
#         guess_count += 1

#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("You're out of guesses!")
# else:    
#     print("You guessed it right!")
    






# For Loops

# for letter in "Mission FireStorm":
#     print(letter) #prints each letter in the string "Mission FireStorm"


# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] #list of friends
# for index in range(len(friends)): #for loop that iterates 3 times        
#     print(friends[index]) #prints each friend in the list

# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] #list of friends
# for index in range(5): #for loop that iterates 5 times
#     if index == 2:
#         print("Third Iteration") #prints "First Iteration" if index is 0
#     else:
#         print("Not First") #prints "Not First" if index is not 0    




# Exponen Function

# print(2 ** 3) #prints the result of 2 raised to the power of 3

# def raise_to_power(base_num, pow_num): #function definition
#     result = 1 #initializing result to 1
#     for index in range(pow_num): #for loop that iterates pow_num times
#         result = result * base_num #multiplying result by base_num
#     return result #returning the result

# print(raise_to_power(3, 4)) #function call that prints the result of 3 raised to the power of 2




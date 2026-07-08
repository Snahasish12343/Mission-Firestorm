# print("Hello world")


#  character_name = "John"
# character_age = "35"
# is_male = True

# print("There once was a man named " + character_name + ",")
# print("he was " + character_age + " years old.")  
# print("He is male: " + str(is_male))

# character_name = "MADISON"
# character_age = 43 #can store numbers as well without quotes
# is_male = False 


# print("There once was a man named " + character_name + ",")
# print("he was " + str(character_age) + " years old.")
# print("He is male: " + str(is_male)) 


# print("Giraffe\nAcademy") #\n is a new line character

# print("Giraffe\"Academy") #\" is used to print quotes in a stringA

# phrase = "Giraffe Academy"
# print(phrase + " is cool") #concatenation of strings

# print(phrase.lower()) #lowercase
# print(phrase.upper().isupper()  ) #uppercase
# print(len(phrase)) #length of string
# print(phrase[0]) #indexing of string    
# print(phrase.index("G")) #find the index of a character
# print(phrase.replace("Giraffe", "Elephant")) #replace a string with another string  


# print (10 % 3) #modulus operator gives the remainder of a division

# my_num = -5
# print(abs(my_num)) #absolute value of a number
# print(pow(3, 2)) #power of a number
# print(max(4, 6)) #maximum of two numbers
# print(min(4, 6)) #minimum of two numbers    
# print(round(3.7)) #rounds a number to the nearest integer
# print(round(3.2)) #rounds a number to the nearest integer
# print(round(3.5)) #rounds a number to the nearest integer










# from math import * #importing all functions from the math module

# print(floor(3.7)) #rounds down to the nearest integer
# print(ceil(3.2)) #rounds up to the nearest integer
# print(sqrt(36)) #square root of a number 





# name = input("Enter your name: ") #input function takes input from the user

# print("Hello " + name + "!") #prints the input taken from the user




# calculator program that takes two numbers as input from the userclr and adds them together

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")  

# result = float(num1) + float(num2) #converting the input to float and adding themq

# print(result) #printing the result of the addition

# mad libs game
# color = input("Enter a color: ")
# noun = input("Enter a noun: ")
# celebrity = input("Enter a celebrity: ")

# print("Roses are " + color)
# print(noun + " are blue")
# print("I love " + celebrity)





# List 



# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] #list of friends
# print(friends)

# print(friends[0]) #prints the first element of the list
# print(friends[1]) #prints the second element of the list    
# print(friends[2]) #prints the third element of the list
# print(friends[1:]) #prints the second element to the end of the list
# print(friends[1:3]) #prints the second and third element of the list

# friends[1] = "Mike" #changing the second element of the list
# print(friends) #prints the updated list


# List function


# lucky_numbers = [4, 8, 15, 16, 22]  
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Jim", "Toby"] #list of friends
# print(friends)
# print(friends.index("Jim")) #prints the index of the element "Jim"
# friends.extend(lucky_numbers) #adds the elements of the list lucky_numbers to the list friends
# print(friends) #prints the updated list

# friends.append("Creed") #adds the element "Creed" to the end of the list
# print(friends) #prints the updated list

# friends.insert(1, "Kelly") #adds the element "Kelly" to the list at index 1
# print(friends) #prints the updated list 

# friends.remove("Jim") #removes the element "Jim" from the list
# print(friends) #prints the updated list

# friends .pop() #removes the last element of the list
# print(friends) #prints the updated list

# print(friends.index("Oscar")) #prints the index of the element "Oscar"

# print(friends.count("Jim")) #prints the number of times the element "Jim" appears in the list

# friends.sort() #sorts the list in ascending order
# print(friends) #prints the sorted list  


# friends = ["Kevin", "Karen", "Jim", "Oscar", "Jim", "Toby"] #list of friends
# friends.sort() #sorts the list in ascending order
# print(friends) #prints the sorted list
# friends.reverse() #reverses the order of the list
# print(friends) #prints the reversed list

# friends2 = friends.copy() #creates a copy of the list friends
# print(friends2) #prints the copied list




# Touples

# coordinates = (4, 5) #tuples are immutable
# print(coordinates[0]) #prints the first element of the tuple
# print(coordinates[1]) #prints the second element of the tuple   

# values in a tuple cannot be changed, added or removed. Tuples are used to store multiple items in a single variable and are defined using parentheses ().

# coordinates = [(4, 5), (6, 7), (80, 34)] #list of tuples
# print(coordinates[0]) #prints the first tuple in the list
# print(coordinates[1]) #prints the second tuple in the list
# print(coordinates[2]) #prints the third tuple in the list   




# Function

# def say_hi():
#     print("Hello User") #function definition    

# print("Top") #prints "Top"
# say_hi() #function call   
# print("Bottom") #prints "Bottom"

# def say_hi(name, age): #function definition
#     print("Hello, " + name + ". You are " + str(age)) #function definition    


# say_hi("Mike", 35) #function call   

# say_hi("Steve", 40) #function call\









# Return Statement

# def cube(num): #function definition
#     return num*num*num #return statement

# result = cube(4) #function call
# print(result) #prints the result of the function call   



# if statements

# is_male = False #boolean variable
# is_tall = True #boolean variable

# if is_male and is_tall: #if statement
#     print("You are a tall male") #prints if both conditions are true

# elif is_male and not is_tall:
#     print("You are a short male") #prints if the first condition is true but the second is false

# elif not is_male and is_tall:
#     print("You are a tall female") #prints if the first condition is false but the second is true

# else:
#     print("You are not a male") #prints if the condition is false





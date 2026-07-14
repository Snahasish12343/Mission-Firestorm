# Advance Python

# Tuples


# mytuple = ("Max", 28, "Dhaka")
# print(mytuple)

# mytuple = ("Max",) #for one element use , at the end  or it will be a string
# print(mytuple)





# mytuple = ("Max", 28, "Dhaka")
# print(mytuple)


# item = mytuple[0]
# print(item)

# item = mytuple[-2]
# print(item)



# mytuple[0] = "Tim" #Tuple cant be changed
# print(mytuple)



# for i in mytuple: 
#     print(i)

# if "Maux" in mytuple:
#     print("Yes")
# else:
#     print("No")




# myt = ('a', 'p', 'p', 'l', 'e')

# print(len(myt))
# print(myt.count('p'))

# print(myt.index('p'))



# mylist = list(myt)  #Same way can make tuple
# print(mylist)


# a  = (1,2,3,4,5,6,7,8,9,10)

# b = a[2:5]

# print(b)



# a = "Max", 28, "Dhaka"

# name, age, city = a


# print(name)






# a  = (0,0,1,2,3,4,4,5,6,7,7)

# i1, *i2, i3 = a


# print(i2)




# import sys
# my_list = [0, 1, 2, "hello", True]
# my_tuple = (0, 1, 2, "hello", True)
# print(sys.getsizeof(my_list), "bytes")
# print(sys.getsizeof(my_tuple), "bytes")


# import timeit

# print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
# print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

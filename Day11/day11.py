# Advance Python

# Set


# s = {1,2,3,4,5,76,5}

# print(s)

# ss = set([1,2,3,4,5,56,5,4,4,4,4,34])
# ss1 = set("Hellooo")
# print(ss)
# print(ss1)

# s = set()

# s.add(1)
# s.add(2)
# s.add(3)
# s.add(3)
# s.add(5)

#s.clear()  will make the set empty
# print(s.pop())
# print(s)


# for i in s:
#     print(i)


# if 1 in s:
#     print("Yes")
# else:
#     print("No")    






# Sets: unordered, mutable,
# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds.union(evens)
# print(u)

# i = odds.intersection(primes)
# print(i)


# i = evens.intersection(primes)
# print(i)


setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# diff =  setA.difference(setB) #diffeference from set A

# diff =  setA.symmetric_difference(setB)            #diffeference from both sets

# print(diff)


# setA.update(setB)

setA.intersection_update(setB) #Oly common Eliments

print(setA)
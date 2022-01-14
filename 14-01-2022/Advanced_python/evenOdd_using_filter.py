'''
syntax ----> filter(function, sequence)

The function filter(f,l) needs a function f as its first argument. 
f has to return a Boolean value, i.e. either True or False. 
This function will be applied to every element of the list l. 
Only if f returns True will the element be produced by the iterator, which is the return value of filter(function, sequence).

'''

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
# odd_numbers = list(filter(lambda x: x % 2, fibonacci))
odd_numbers = list(filter(lambda x: x % 2 != 0, fibonacci))
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
# even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
print(even_numbers)
print(odd_numbers)
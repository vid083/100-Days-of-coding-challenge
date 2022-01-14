'''
syntax ---> r = map(func, seq)

The first argument func is the name of a function and 
the second a sequence (e.g. a list) seq. map() applies the function func to all the elements of the sequence seq. 
Before Python3, map() used to return a list, 


str = '2324'
sliced_num = int(str)
print(sliced_num)
li = sum(list(sliced_num))
# print(li)
'''

str1="987654321"
list1=list(str1.split())
list2=list(map(int,list1))
list3=sum(list2)
print(list3)
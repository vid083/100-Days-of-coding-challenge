'''
syntax ----> reduce(func, seq)

continually applies the function func() to the sequence seq. 
It returns a single value.

'''


from functools import reduce
f = lambda a,b: a if (a > b) else b
print(reduce(f, [47,11,42,102,13]))


print(reduce(lambda x,y: x+y, [47,11,42,13]))


print(reduce(lambda x, y: x+y, range(1,49)))
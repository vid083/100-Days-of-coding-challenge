'''
#Efficient solution

def power(x,n):
    if n==0:
        return 1
    
'''

#naive solution

def power(x,n):
    res = 1
    i = 0
    while i < n:
        res = res * x
        i = i+1
    return res
print(power(3,4))
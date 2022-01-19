'''
# recursive

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))
'''

# iterative

def fact(n):
    res = 1
    i = 2
    while i < n:
        res = res*i
        i = i+1
        return res
print(fact(5))




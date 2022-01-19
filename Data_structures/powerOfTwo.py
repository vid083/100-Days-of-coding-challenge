# recursive

def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

print(powerOfTwo(3))

'''
#iterative solution

def powerOfTwo(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i+1
    return power

print(powerOfTwo(3))

# iterations:
i=0, power=1
    0<3, power=1*2=2, i=0+1=1

i=1, power=2
    1<3, power=2*2=4, i=1+1=2

i=2, power=4
    2<3, power=4*2=8, i=2+1=3

i=3, power=8
    3<3, return 8
'''




'''
for given AP, find the sum of first hundred and print the 90th position number

Sn = n/2[2a+(n-1)d]
n = 100
a = 1
d = 1

Tn = a + (n-1)d
'''

def ap(sum_n,position):
    sum_n = 100
    a = 1
    d = 1
    Sn = (sum_n/2)*((2*a)+(sum_n-1)*d)
    print("Sn :", int(Sn))

    Tn = a+((position-1)*d)
    print("Tn :",Tn)


ap(100,90)

'''
for given angles, return whether its is a triangle or not
[30,60,90] --- true
[30,60,91] --- false
'''

def triangle_verify(A1,A2,A3):
    a1 = int(A1)
    a2 = int(A2)
    a3 = int(A3)

    if a1 + a2 + a3 == 180 :
        print(True)
    else:
        print(False)


triangle_verify(input("Enter A1 :"),input("Enter A2 :"),input("Enter A3 :") )
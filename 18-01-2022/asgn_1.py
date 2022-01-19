"""
for a given length of a triangle, return whether its is a triangle or not
triangle_verify([3,4,5]) -- true
triangle_verify([3,4,8]) -- false
triangle_verify([4,5,3]) -- true
triangle_verify([4,8,3]) -- false
hint: sum of two sides is always greater than other side

"""

def triangle_verify(L1,L2,L3):
    l1 = int(L1)
    l2 = int(L2)
    l3 = int(L3)

    if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
        print(True)
    else:
        print(False)


triangle_verify(input("Enter l1 :"),input("Enter l2 :"),input("Enter l3 :") )

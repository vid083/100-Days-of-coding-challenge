'''
    *
  * * *
* * * * *
  * * *
    *


1. for loop
2. n i
3. if i < n/2  : a = 

i=0 , n+1//2 = 3, 2(i+1)-1 = *
i=1,  n+1//2 = 3, 2(i+1)-1 = * * *
i=2,  n+1//2 = 3, 2(i+1)-1 = * * * * *
 
i=3,  n+1//2 = 3, 2(i-1)-1 = * * *
i=4,  n+1//2 = 3, 2(i-1)-1 = *
 4 --> 1,  3 --> 
'''

n = 7

for i in range(n):
    if i <= n//2:
        cond_n = (n)//2
        star_count = n-2*(cond_n-i)
        # print(i)
        print(f"for i = {i}, condition = {cond_n} , stars = {star_count}")
    else:
        cond_n = (n)//2
        star_count = n-2*(i-cond_n)
        # print(i)
        print(f"for i = {i}, condition = {cond_n} , stars = {star_count}")


'''
space design,
 j loop
'''
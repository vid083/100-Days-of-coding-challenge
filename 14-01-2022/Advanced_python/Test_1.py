'''
Let us assume given number = 12345789899, find four adjacent digits which has largest sum
All of 4 digit adjacent numbers extracted from number is: 1234, 2345, 3457, 4578, 5789, 7898, 8989, 9899
From these 4 digit adjacent numbers, 9899 has highest sum = 9 +8+9+ 9 = 35
'''

def largest_sum(n):
    # print(n)
    n = str(n)
    largest = 0
    for i in range(len(n)):
        if len(n[i:i+4]) == 4: # for string length = 4
            print(n[i:i+4])
            sub_string = n[i:i+4]
            
            sum_of_num = 0
            li = list(map(int,sub_string))
            sum_of_num = sum(li)
            if sum_of_num > largest:
                largest = sum_of_num
    print(sum_of_num)


largest_sum(123456789999)

'''
            sum = 0
            for j in sub_string:
                sum += int(j)
            if sum > largest: 
                largest = sum
        # print(sum)
    print("largest number: ",largest)
        
largest_sum(73167891129494951569329093999953362766142828064444860)


---------------------------
flow chart and break down:

1. convert number to string
2. for loop for slicing numbers
3. for loop to add numbers in sliced number --or-- convert str to list then find list sum
4. find largest of the sum of digits in sliced number

'''
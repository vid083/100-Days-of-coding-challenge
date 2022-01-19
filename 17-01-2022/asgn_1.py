


'''
for given time find the angles b/w hours dial and min dial 
angle_cal("3:00") -- o/p : 90
angle_cal("6:00") -- o/p : 180
angle_cal("12:00") -- o/p : 0 

hours = 360 * 12 = 30
min = 360 /60 = 6
3:05 --> 30 * 3 = 90 
     ---> 6 * 5 = 30
     --> 60

3:25 --> 30 * 3 = 90
     --> 6 * 25 = 150
     --> angle: 60

7:40 --> 30 * 7 = 210
     --> 6 * 40 = 240
     --> angle: 30
'''

def angle_cal(time):
    li = time.split(":")
    print(li)
    hours = 30
    min = 6
    a = hours * int(li[0])
    b = min * int(li[1])
    print(f"a={a}, b={b}")
    angle = abs(a-b)
    print("angle =",angle)
    return angle


angle_cal(input("Enter desired time: "))
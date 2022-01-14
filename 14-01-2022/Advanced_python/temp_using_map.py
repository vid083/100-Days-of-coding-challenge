'''
C = [39.2, 36.5, 37.3, 38, 37.8] 
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)


'''
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)

temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))

print(temperatures_in_Fahrenheit)
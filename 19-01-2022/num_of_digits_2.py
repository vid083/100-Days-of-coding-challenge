# recursive method

def num_of_digits(n):
    if n == 0:
        return 0
    else:
        return 1+num_of_digits(n/10)


print(num_of_digits(n))

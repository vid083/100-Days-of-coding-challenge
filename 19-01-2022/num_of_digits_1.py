#
# iterative solution

def num_of_digits(n):
    count = 0
    while n > 0:
        n = int(n/10)
        print(n)
        count += 1
    print(count)


num_of_digits(123456)
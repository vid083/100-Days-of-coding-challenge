def check_prime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2 == 0 or n%3==0:
        return False
    for i = 5
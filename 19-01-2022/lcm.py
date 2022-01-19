def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return (a*b)/gcd(a,b)

print(lcm(4,6))

# a*b = gcd(a,b)*lcm(a,b)
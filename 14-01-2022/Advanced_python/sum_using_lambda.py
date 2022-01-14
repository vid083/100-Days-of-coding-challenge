'''
Syntax ----> lambda argument_list: expression

The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments. You can assign the function to a variable to give it a name.

The following example of a lambda function returns the sum of its two arguments:

'''

sum = lambda x,y : x+y
print(sum(3,4))


'''
def sum(x,y):
    sum = x+y
    return sum

sum(3,4)
'''
# input: 253
# output: 10

def fun(n):
    if (n < 10):
        return n
    return fun(n//10) + n % 10


    
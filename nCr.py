def nCr(n,r):
    def fact(x):
        if(x <= 0):
            return 1
        return x*fact(x-1)
    return fact(n)/(fact(n-r)*fact(r))

print(nCr(5,2))
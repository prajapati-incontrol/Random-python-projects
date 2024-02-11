import math

def isprime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    
    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def primfact(n):
    # find all the prime factors of n
    # 100 >> 2, 2, 5, 5
    for i in range(2,n+1):
        if isprime(i):
            x = i
            while (n % x == 0):
                print(i)
                x = x * i
    
            
            
                
               
print(primfact(127))
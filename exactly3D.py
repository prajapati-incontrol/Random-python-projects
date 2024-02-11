import math 

def ip(n):
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
    

class Solution:
    
    def exactly3Divisors(self,n):
        soln = 0
        i = 2
        while i * i <= n:
            if (ip(i)):
                if (i*i <= n):
                    soln += 1
            i += 1
        return soln
import math
import time

# find the prime numbers less than that number
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

def naive(n):
    for i in range(2,n+1):
        if isprime(i):
            print(i)

def sieve(n):
    if n <= 1:
        return 
    isPrime = [True]*(n+1)
    
    i = 2
    while i*i <= n:
        if isPrime[i]:
            for j in range(2*i, n+1, i):
                # Falsify all the non prime numbers, or the multiples of i less than n
                isPrime[j] = False
        i += 1
        
    for i in range(2,n+1):
        if isPrime[i]:
            print(i)   

N = 100000    
t = time.time()
naive(N)
elapsed = time.time() - t

print("\n")

t = time.time()
sieve(N)
elapsed2 = time.time() - t

print(elapsed, "\n")
print(elapsed2)
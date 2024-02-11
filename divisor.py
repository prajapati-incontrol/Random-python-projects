import time
# Naive Solution
def all_div1(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i)

# Efficient solution
"""
1. Divisors always appear in PAIRS
Ex: 30: (1,30), (2,15), (3,10)...

2. One of the divisors in every pair is smaller than or equal to sqrt(n)
"""

def effdiv(n):
    i = 1
    while(i*i <= n):
        if (n % i == 0):
            print(i)
        i += 1
    i = i - 2
    while (i >= 1):
        if (n % i == 0):
            print(int(n/i))
        i -= 1

# driver code
if __name__ == "__main__":
    t = time.time()
    effdiv(1320)
    elapsed1 = time.time() - t
    
    t2 = time.time()
    all_div1(10000000)
    elapsed2 = time.time() - t2
    
    print("\n")
    print(elapsed1)
    print("\n")
    print(elapsed2)
    
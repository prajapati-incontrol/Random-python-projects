def fact(n):
    value = n
    while n-1 > 0:
        value = value*(n-1)
        n = n - 1
    return value

def fact_recurs(n):
    return 1 if (n == 1 or n == 0) else n*fact_recurs(n-1)

def digitsInFactorial(n):
    # code here
    value = n
    while (n-1) > 0:
        value *= (n-1)
        n = n-1
        
    if (n == 0):
        value = 1 
    
    count = 0
    while value > 0:
        count += 1
        value //= 10 
    return count
            
# Driver Code:
if __name__ == "__main__":
    print(fact(4))
    print(digitsInFactorial(5))
    
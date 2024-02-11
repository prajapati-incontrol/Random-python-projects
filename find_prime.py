import math

def isPrime(n):
    # Corner case
    if (n <= 1):
        return "No"
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            return "No"
 
    return "Yes"
    

if __name__ == '__main__':
    print(isPrime(32))

    
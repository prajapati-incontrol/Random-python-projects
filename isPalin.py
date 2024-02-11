import math

def isPalin(N):
    def rev(N):
        if (N<10):
            return N
        return (N%10)*10**int(math.log10(N)) + rev(N//10)
    print(rev(N))
    if rev(N) == N:
        return True
    else:
        return False
    
print(isPalin(1001))
print(1*int(math.log10(1001)))
# function identify if it is a palindrome
def isPal(n):
    rev = 0
    temp = n
    while temp != 0:
        ld = temp % 10
        rev = rev*10 + ld
        temp = temp // 10
    return rev == n

# A Python programme uses the condition if __name__ == '__main__' to only
# run the code inside the if statement when the program is
# run directly by the Python interpreter.
# Driver Code:
if __name__ == '__main__':
    print(isPal(57875))
    print(isPal(445))


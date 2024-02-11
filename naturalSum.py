x = int(input("Enter a number = "))

def get_sum(x):
    gsum = x*(x+1)/2
    return gsum 

print("Sum of first " + str(x) + " numbers = ")
print(get_sum)
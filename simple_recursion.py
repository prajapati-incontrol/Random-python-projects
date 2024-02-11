def fun(n):
    if n == 1:
        return 
    for i in range(n):
        print("i")
    fun(int(n/2))
    
def fun2(n):
    if n == 1:
        return 
    print(n)
    fun2(n-1)
    
fun(5)
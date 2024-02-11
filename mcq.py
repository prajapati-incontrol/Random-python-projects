def foo(x):
    if x > 0:
        return (x+foo(x-2))
    else:
        return 0
    
print(foo(10))

l = [10,20,20,30]
print(l.index(20))

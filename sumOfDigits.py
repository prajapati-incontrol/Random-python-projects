def sod(d):
    if d < 10:
        return d
    return sod(d//10) + d % 10

print(sod(1))
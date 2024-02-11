def printArray(arr,n):
    if n == 0:
        return
    print(arr[0], end = " ")
    del arr[0]
    return printArray(arr,len(arr))

myArr = [1,2,3,4,5]
printArray(myArr, len(myArr))
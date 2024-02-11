def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

A = [1,2,3,4,5,6]
index = search(A, 4)
print(index)
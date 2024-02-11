# to count the inversions in an array
# two elements a[i] and a[j] form an inversion 
# if a[i] > a[j] and i < j

# Naive approach
def getInvCount(arr):
    n = len(arr)
    icount = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                icount += 1
    return icount

arr = [6,5,4,8]
print(getInvCount(arr))

# Using merge sort python
def mergeSort(arr, n):
    # A temp_arr is created to store the sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)
                
    
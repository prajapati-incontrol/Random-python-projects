import time

def bubbleSort(arr):
    n = len(arr)
    
    # to search through array
    for i in range(n-1):
        # to swap the unsorted remaining ones
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                
def selectSort(arr):
    n = len(arr)
    
    # start with the array
    for i in range(n-1):
        min_ind = i
        # start with the unsorted array
        for j in range(i+1,n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        # after for loop finds the min of the remaining unsoreted array, 
        # allocate the min to the starting position i
        # swap!
        arr[min_ind], arr[i] = arr[i], arr[min_ind]           

def insertionSort(arr):
    for i in range(1,len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = x



myarr = [47,8,5,4,9,322,74,52,6,3,77,4,1,5,2,6,7,8,52,1,3,5,5,1,44,2,5,42,5,4,8,7,6,9,8,47,14,89,41,84,654,77,8,4,35,1,87,54,84,6,4,654,64,654,987,84,61,654,945,1,894,94,984,9489,49,4984,984]
t = time.time()
bubbleSort(myarr)
print(myarr)
elapsed = time.time() - t


myarr = [47,8,5,4,9,322,74,52,6,3,77,4,1,5,2,6,7,8,52,1,3,5,5,1,44,2,5,42,5,4,8,7,6,9,8,47,14,89,41,84,654,77,8,4,35,1,87,54,84,6,4,654,64,654,987,84,61,654,945,1,894,94,984,9489,49,4984,984]
t = time.time()
insertionSort(myarr)
print(myarr)
elapsed2 = time.time() - t


myarr = [47,8,5,4,9,322,74,52,6,3,77,4,1,5,2,6,7,8,52,1,3,5,5,1,44,2,5,42,5,4,8,7,6,9,8,47,14,89,41,84,654,77,8,4,35,1,87,54,84,6,4,654,64,654,987,84,61,654,945,1,894,94,984,9489,49,4984,984]
t = time.time()
selectSort(myarr)
print(myarr)
elapsed3 = time.time() - t

print(f"Elapsed time using Bubble Sort: {elapsed*10**6}")
print(f"Elapsed time using Insertion Sort: {elapsed2*10**6}")
print(f"Elapsed time using Selection Sort: {elapsed3*10**6}")


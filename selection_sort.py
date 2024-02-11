# Time Complexity O(n^2) worst case
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
    return arr

my_arr = [2,3,5,2,1,3,5,3,45,6,8]
print(selectSort(my_arr))
    
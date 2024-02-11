# Time Complexity O(n^2)
def bubbleSort(arr):
    n = len(arr)
    
    # to search through array
    for i in range(n-1):
        # to swap the unsorted remaining ones
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                
my_arr = [5,2,4,4,9,78,2,3,1,6,4]

bubbleSort(my_arr)
print(*my_arr)


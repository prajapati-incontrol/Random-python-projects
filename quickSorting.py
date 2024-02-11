import time

# using list comprehensions
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        print(pivot)
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)
    
t = time.time()

# example usage
arr = [1,7,4,1,10,9,-2]
sorted_arr = quickSort(arr)
print("Sorted Array in Ascending Order: ")
print(sorted_arr)

elapsed = time.time() - t
print(str(elapsed) + " sec Elapsed")
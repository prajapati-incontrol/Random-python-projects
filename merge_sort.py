def mergeSort(arr, l, r):
    if r > l:
        m = (r+l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, h):
    left = arr[l:m+1]
    right = arr[m+1:h+1]
    i = 0
    j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = right[j]
            k = k + 1
            j = j + 1
    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        
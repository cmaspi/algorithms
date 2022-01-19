# iterate through the array, find the minimum element, swap it with the first element. Now consider the array to be subarray of original array

def selectionsort(array):
    arr = array.copy()
    n = len(arr)
    for i in range(n-1):
        min,minI = arr[i] , i
        for j in range(i+1,n):
            if arr[j]<min:
                min = arr[j]
                minI = j
        temp = min
        arr[minI] = arr[i]
        arr[i] = temp
    return arr
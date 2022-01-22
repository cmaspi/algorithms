# This algorithms runs in O(sqrt(n)) time,
# it takes jumps of sqrt(n) and find the interval in which the element could be there
import numpy as np
def jumpSearch(arr, element):
    n = len(arr)
    step = int(np.sqrt(n))
    i = step
    prev = 0
    while i<n:
        if arr[i]>element:
            break
        i+=step
        prev += step
    while prev < min(i,n):
        if arr[prev] == element:
            return prev
        prev+=1
    return -1

        
    





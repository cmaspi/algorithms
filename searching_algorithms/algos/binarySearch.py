# binary search is a divide and conquer algorithm,
# it would search for the element in the subarray in which it should be there

def binarysearch(arr, element):
    n = len(arr)
    m = n//2
    if arr[m] == element:
        return m
    if n == 1:
        return -1 # this would happen when the element is not what we want
    if arr[m]>element:
        return binarysearch(arr[:m],element)
    else:
        ret = binarysearch(arr[m+1:],element)
        return (m+1+ret) if ret!=-1 else -1

     
    
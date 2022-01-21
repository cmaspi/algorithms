# merge sort is a divide and conquer alogithm, that runs in O(n log(n)). The array is divided into two subarrays, then merge sort is called recursively, then the two subarrays are merged by merge function

def mergesort(array, cmpfunc=None, inplace = False):
    if cmpfunc is None or cmpfunc == 'asc':
        cmpfunc = lambda x,y: x<y
    elif cmpfunc == 'desc':
        cmpfunc = lambda x,y: x>y
    if inplace:
        arr = array
    else:
        arr = array.copy()
    n = len(arr)
    if n==1:
        return arr
    m = n//2
    arr[:m] = mergesort(arr[:m], cmpfunc, True)
    arr[m:] = mergesort(arr[m:], cmpfunc, True)
    arr = merge(arr,m)
    return arr

def merge(arr,m):
    arr1 = arr[:m].copy()
    arr2 = arr[m:].copy()
    itr1, itr2 = 0, 0
    len1, len2 = len(arr1), len(arr2)
    while itr1<len1 and itr2<len2:
        if arr1[itr1]< arr2[itr2]:
            arr[itr1+itr2]=arr1[itr1]
            itr1+=1
        else:
            arr[itr1+itr2] = arr2[itr2]
            itr2+=1
    while itr1!=len1:
        arr[itr1+itr2] = arr1[itr1]
        itr1+=1
    while itr2!=len2:
        arr[itr1+itr2] = arr2[itr2]
        itr2+=1
    return arr
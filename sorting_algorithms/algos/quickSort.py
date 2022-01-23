# Quick sort is a divide and conquer algorithm, it works on the principle of sorting array around pivot, the elements smaller than pivot go to the left of the pivot

def quicksort(array, cmpfunc=None ,inplace=False):
    if cmpfunc is None or cmpfunc == 'asc':
        cmpfunc = lambda x,y : x<y
    elif cmpfunc == 'desc':
        cmpfunc = lambda x,y : x>y
    if inplace:
        arr = array
    else:
        arr = array.copy()
    n = len(arr)
    if n == 1 or n == 0:
        return arr
    pivot = arr[-1]
    i = 0
    for j in range(n):
        if arr[j]<=pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i+=1
    i-=1
    arr[:i] = quicksort(arr[:i],cmpfunc,True)
    arr[i+1:] = quicksort(arr[i+1:],cmpfunc,True)
    return arr
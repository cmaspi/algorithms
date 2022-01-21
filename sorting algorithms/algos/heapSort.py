

def heapify(arr, i, n, cmpfunc):
    l = 2*i+1
    r = l+1
    largest = i
    if l<n and cmpfunc(arr[largest],arr[l]):
        largest = l
    if r<n and cmpfunc(arr[largest], arr[r]):
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i] , arr[largest]
        heapify(arr, largest, n, cmpfunc)

def heapsort(array, cmpfunc=None, inplace=False):
    if inplace:
        arr = array
    else:
        arr = array.copy()
    if cmpfunc is None or cmpfunc == 'asc':
        cmpfunc = lambda x,y: x<y
    elif cmpfun == 'desc':
        cmpfunc = lambda x,y: x>y
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,i,n,cmpfunc)
    for i in range(n-1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr,0,i,cmpfunc)

    return arr

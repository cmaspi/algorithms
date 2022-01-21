# it runs in O(nlogn) time, the idea is to heapify the nodes starting from n//2-1 index all the way up to root, making it off opposite order as to what is required, such as if we want to sort in ascending order, build a max heap. 
# then swap the last element with the root, just like you would delete it, we are sort of building a stack here.
# then heapify the root but don't consider the last element in the array, similarly go on doing this again and again, everytime we heapify we would extract the max element from the heap (swap it with last element of our current array(which is a subarray))

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

# iterate through the array till it is sorted, in each iteration compare adjacent values and swap them if required.

def bubblesort(array, cmpfunc=None):
    if cmpfunc is None:
        cmpfunc = lambda x,y: x<y
    if cmpfunc == 'desc':
        cmpfunc = lambda x,y: x>y
    arr = array.copy()
    n = len(array)
    notSorted = True
    while notSorted:
        notSorted = False
        for i in range(n-1):
            if cmpfunc(arr[i+1], arr[i]):
                arr[i] = arr[i+1]+arr[i]
                arr[i+1] = arr[i]-arr[i+1]
                arr[i] = arr[i]- arr[i+1]
                notSorted = True
    return arr
# insertion sort is a sorting algorithm that runs in O(n^2) time.
# take the subarray a[:i] (i goes from 1 to n), take the last element, if it is less than the element before it, then check for element before it and so on and so forth, when it is no longer less than the previous one or theere are no more elements in the array, put the element in that position and shift the array by 1

def insertionsort(array , cmpfunc=None):
    if cmpfunc is None or cmpfunc == 'asc':
        cmpfunc = lambda x,y: x<y
    elif cmpfunc == 'desc':
        cmpfunc = lambda x,y: x>y
    arr = array.copy()
    n = len(arr)
    for i in range(1,n):
        if cmpfunc(arr[i],arr[i-1]):
            j=i-1
            while j>=0 and cmpfunc(arr[i],arr[j]):
                j-=1
            j+=1
            temp = arr[i]
            k = i-1
            while k!=j-1:
                arr[k+1] = arr[k]
                k-=1
            arr[j] = temp
    return arr
            

    
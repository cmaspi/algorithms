# counting sort works in n+k time
# here k is the number range of the array, n is the number of elements in the array
# count the number of times each element is appearing, 
# calculate cumulative sum, then 
# then start from backward and put elements in the new array

def countingsort(array, cmpfunc=None, inplace=False):
    if inplace:
        arr = array
    else:
        arr = array.copy()
    n = len(arr)
    max = min = arr[0]
    for i in range(n):
        if min>arr[i]:
            min = arr[i]
        elif max<arr[i]:
            max = arr[i]
    k = max-min+1
    count = [0]*(k)
    for i in range(n):
        count[arr[i]-min] += 1
    if cmpfunc == 'asc' or cmpfunc is None:
        for i in range(1,k):
            count[i]+=count[i-1]
    else:
        for i in range(k-2,-1,-1):
            count[i] += count[i+1]
    ret = arr.copy()
    for i in range(n-1,-1,-1):
        ret[count[arr[i]-min]-1] = arr[i]
        count[arr[i]-min] -= 1
    return ret

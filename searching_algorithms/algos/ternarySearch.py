# it is just like binary search but uses two middle points

def ternarysearch(arr, element):
    n = len(arr)
    m1 = n//3
    m2 = (2*n)//3
    if n==0 :
        return -1
    if arr[m1] == element:
        return m1
    if arr[m2] == element:
        return m2
    if n ==2 :
        return -1
    if arr[m1]>element:
        return ternarysearch(arr[:m1],element)
    elif arr[m2]<element:
        ret = ternarysearch(arr[m2+1:],element)
        return (m2+1+ret) if ret !=-1 else -1
    else:
        ret = ternarysearch(arr[m1+1:m2], element)
        return (m1+1+ret) if ret !=-1 else -1
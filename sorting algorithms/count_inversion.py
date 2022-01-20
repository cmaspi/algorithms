# Count inversion is a problem in which we have to find how close an array is to being sorted.
# in other words
# total number of pairs of indices i,j such that a[i]>a[j] while i<j

# brute force
# Iterate through the array arr[i:] for i in range(n-1), in each iteration count the number of such pairs with index i element as one constant in the pair.

import numpy 

def bruteForce(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                count+=1
    return count

def mergeSort(array):
    arr =array.copy()
    n = len(arr)
    count = 0
    if n==1:
        return arr,count
    m = n//2
    arr[:m], ctemp1 = mergeSort(arr[:m])
    arr[m:], ctemp2 = mergeSort(arr[m:])
    count += (ctemp1+ctemp2)
    itr1, itr2 = 0,0
    len1,len2 = m,n-m
    arr1 = arr[:m].copy()
    arr2 = arr[m:].copy()
    while itr1!=len1 and itr2!=len2:
        if arr1[itr1]<arr2[itr2]:
            arr[itr1+itr2] = arr1[itr1]
            itr1+=1
        else:
            arr[itr1+itr2] = arr2[itr2]
            itr2+=1
            count+= m-itr1
    while itr1!=len1:
        arr[itr1+itr2] = arr1[itr1]
        itr1+=1
    while itr2!=len2:
        arr[itr1+itr2] = arr2[itr2]
        itr2+=1
    return arr,count


if __name__ == '__main__':
    unsorted =  numpy.array([3,8,5,7,1,6,4])
    print(bruteForce(unsorted))
    print(mergeSort(unsorted)[1])

# time complexity is O(n)
# We linearly search for the element, if it is not found, we return -1, otherwise we return the index of the element.

def linearsearch(arr, element):
    n = len(arr)
    for i in range(n):
        if arr[i]== element:
            return i
    return -1
    
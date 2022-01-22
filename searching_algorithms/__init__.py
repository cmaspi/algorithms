import numpy as np
import algos.linearSearch as ls
import algos.binarySearch as bs
import algos.ternarySearch as ts
import algos.jumpSearch as js

class searching:
    def __init__(self) -> None:
        self.sorted = np.array([2,4,5,8,13,17,32])
    def linearSearch(self, array, element):
        return ls.linearsearch(array,element)
    def binarySearch(self, array, element):
        return bs.binarysearch(array, element)
    def ternarySearch(self, array, element):
        return ts.ternarysearch(array, element)
    def jumpSearch(self, array, element):
        return js.jumpSearch(array, element)

search = searching()
print(search.linearSearch(search.sorted, 32))
print(search.binarySearch(search.sorted, 13))
print(search.ternarySearch(search.sorted, 4))
print(search.jumpSearch(search.sorted, 32))

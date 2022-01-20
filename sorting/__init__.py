# import statements
import numpy as np
import selectionSort as ss
import bubbleSort as bs
import insertionSort as Is

class sorting:
    def __init__(self) -> None:
        self.unsorted = np.array([3,2,5,1,6,4])
        
    def selectionSort(self,arr: np.array, cmpfunc=None):
        return ss.selectionsort(arr, cmpfunc)

    def bubbleSort( self, arr: np.array, cmpfunc=None):        
        return bs.bubblesort(arr, cmpfunc)
    
    def insertionSort( self, arr: np.array, cmpfunc=None):
        return Is.insertionsort(arr, cmpfunc)    

sort = sorting()
print(sort.selectionSort(sort.unsorted))
print(sort.bubbleSort(sort.unsorted))
print(sort.insertionSort(sort.unsorted))

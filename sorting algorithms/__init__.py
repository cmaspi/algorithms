# import statements
import numpy as np
import algos.selectionSort as ss
import algos.bubbleSort as bs
import algos.insertionSort as Is
import algos.mergeSort as ms

class sorting:
    def __init__(self) -> None:
        self.unsorted = np.array([3,2,5,1,6,4])
        
    def selectionSort(self,arr: np.array, cmpfunc=None):
        return ss.selectionsort(arr, cmpfunc)

    def bubbleSort( self, arr: np.array, cmpfunc=None):        
        return bs.bubblesort(arr, cmpfunc)
    
    def insertionSort( self, arr: np.array, cmpfunc=None):
        return Is.insertionsort(arr, cmpfunc)    

    def mergesort(self, arr:np.array, cmpfunc=None):
        return ms.mergesort(arr,cmpfunc)
sort = sorting()
print(sort.selectionSort(sort.unsorted))
print(sort.bubbleSort(sort.unsorted))
print(sort.insertionSort(sort.unsorted))
print(sort.mergesort(sort.unsorted))


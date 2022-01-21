# import statements
import numpy as np
import algos.selectionSort as ss
import algos.bubbleSort as bs
import algos.insertionSort as Is
import algos.mergeSort as ms
import algos.quickSort as qs
import algos.heapSort as hs

class sorting:
    def __init__(self) -> None:
        self.unsorted = np.array([3,2,5,1,6,4])
        
    def selectionSort(self,arr: np.array, cmpfunc=None):
        return ss.selectionsort(arr, cmpfunc)

    def bubbleSort( self, arr: np.array, cmpfunc=None):        
        return bs.bubblesort(arr, cmpfunc)
    
    def insertionSort( self, arr: np.array, cmpfunc=None):
        return Is.insertionsort(arr, cmpfunc)    

    def mergeSort(self, arr:np.array, cmpfunc=None):
        return ms.mergesort(arr,cmpfunc)
    
    def quickSort(self, arr: np.array, cmpfunc=None):
        return qs.quicksort(arr,cmpfunc)
    
    def heapSort(self, arr:np.array, cmpfunc=None):
        return hs.heapsort(arr,cmpfunc)

sort = sorting()
print(sort.selectionSort(sort.unsorted))
print(sort.bubbleSort(sort.unsorted))
print(sort.insertionSort(sort.unsorted))
print(sort.mergeSort(sort.unsorted))
print(sort.quickSort(sort.unsorted))
print(sort.heapSort(sort.unsorted))


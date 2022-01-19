# import statements
import numpy as np
import selectionSort as ss

class sorting:
    def __init__(self) -> None:
        self.unsorted = np.array([3,2,5,1,6,4])
        
    def selectionSort(self,arr: np.array=None):
        if arr is None:
            arr = self.unsorted
        return ss.selectionsort(arr)

sort = sorting()
print(sort.selectionSort())

class Solution:
    def isSorted(self,arr,n):
        #code here
        arr1 = sorted(arr)
        arr2 = sorted(arr, reverse=True)
        if (arr == arr1 or arr == arr2):
            return 1
        else:
            return 0
#give input accordingly

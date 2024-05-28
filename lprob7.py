class Solution:
    def immediateSmaller(self,arr,n,x):
        #return required ans
        smaller = -1
        for i in arr:
            if 0<x-i<x-smaller:
                smaller = i
        return smaller
        #code here

class Solution:
    # inf has been imported in driver code
    def immediateGreater(self,arr,n,x):
        #return required ans
        result = [i-x for i in arr if i-x>0]
        result.sort()
        if not result:
            return -1
        img = result[0]+x
        return img 
#give input accordingly 

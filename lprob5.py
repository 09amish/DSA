import math
class Solution:
    ##Complete the below codes
    #Function to find median of the array elements.
    def median(self,A,N):
        
        A.sort()
        if N%2!=0:
            return math.floor(A[(N)//2])
        else:
            return math.floor((A[(N//2)]+A[(N-1)//2])/2)
        
        ##Your code here
        #If median is fraction then convert the median to integer and return
     
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        ##Your code here
        return math.floor(sum(A)/N)

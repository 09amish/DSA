class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):

        D %= N  # To handle cases where D is greater than N
        
        # Function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        
        # Rotate the array
        reverse(0, D - 1)
        reverse(D, N - 1)
        reverse(0, N - 1)

#give input accordingly

class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, n, x, y):
        # code here
        count_x = 0
        count_y = 0
        
        # Count occurrences of x and y in the array
        for num in arr:
            if num == x:
                count_x += 1
            elif num == y:
                count_y += 1
        
        # If both elements have the same frequency, return the smaller element
        if count_x == count_y:
            return min(x, y)
        # Otherwise, return the element with higher frequency
        elif count_x > count_y:
            return x
        else:
            return y
#give input accordingly

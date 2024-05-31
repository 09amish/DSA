def sumExists(arr, N, sum):
    ##Your code here
    seen = set()
    for num in arr:
        complement = sum - num
        if complement in seen:
            return 1
        seen.add(num)
    return 0
      #write code accordingly

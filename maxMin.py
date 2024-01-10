#function to get max and min sum values
def maxMin(arr):
   arr.sort()
   min_sum = sum(arr[:-1])
   max_sum = sum(arr[1:])
   return min_sum, max_sum
   


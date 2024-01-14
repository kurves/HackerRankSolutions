import random
import math
def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    min_sum = sum(sorted_arr[:-1])
    max_sum = sum(sorted_arr[1:])
    print(min_sum, max_sum)
    print(sorted_arr)

miniMaxSum([1,5,7,9,3])
import random
import math
def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    min_sum = sum(arr[1:])
    four_num = random.sample(arr,4)
    min_sum = sum(four_num)
    print(min_sum)
    print(sorted_arr)

miniMaxSum([1,5,7,9,3])
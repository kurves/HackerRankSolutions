import random
import math
def miniMaxSum(arr):
    four_num = random.sample(arr,4)
    min_sum = math.min(sum(four_num))
    print(min_sum)
    print(four_num)

miniMaxSum([1,3,5,7,9])
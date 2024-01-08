#function to get max and min sum values
def maxMin(arr):
    sum =0
    for i in arr:
        for j in arr:
            total = sum([i][j])
            print(total)


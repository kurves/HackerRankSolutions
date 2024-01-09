#function to get max and min sum values
def maxMin(arr):
    num = 4
    for i in arr:
        if i == 4:
            break
    sum =0
    for i in arr:
        for j in arr:
            total = sum([i][j])
            print(total)

